import unittest
from click.testing import CliRunner
from digital_twin import main, simulate

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
