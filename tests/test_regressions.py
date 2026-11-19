import unittest
from unittest.mock import patch
from click.testing import CliRunner
from digital_twin import Module, Rack, main, simulate

class SimulationTests(unittest.TestCase):
    def test_seed_reproduces_cli_output(self):
        runner = CliRunner()
        args = ["--modules", "2", "--simulation-runs", "100", "--seed", "42"]
        first = runner.invoke(main, args)
        self.assertEqual(first.exit_code, 0, first.output)
        self.assertEqual(first.output, runner.invoke(main, args).output)

    def test_invalid_runs(self):
        with self.assertRaises(ValueError):
            simulate([], runs=0)
        self.assertNotEqual(CliRunner().invoke(main, ["--modules", "0"]).exit_code, 0)


    def test_invalid_module_input_is_rejected(self):
        for module in (
            Module([Rack(1, 1)], 0, 1),
            Module([Rack(1, float("inf"))], 1, 1),
            Module([Rack(-1, 1)], 1, 1),
            Module([Rack(1, 1)], 1, float("nan")),
        ):
            with self.subTest(module=module), self.assertRaises(ValueError):
                simulate([module])
        with self.assertRaises(ValueError):
            simulate([])

    @patch.object(Module, "is_failed", return_value=False)
    def test_exact_capacity_succeeds_and_overload_fails(self, _failure):
        self.assertEqual(simulate([Module([Rack(10, 10)], 10, 10)]), 1.0)
        self.assertEqual(simulate([Module([Rack(10, 11)], 10, 10)]), 0.0)
