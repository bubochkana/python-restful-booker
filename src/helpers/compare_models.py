from typing import Dict, Any, List


class CompareModel:
    def __init__(self):
        ignore_order = False
        self.comparison_results: List[str] = []

    def compare_dicts(self, expected_results: Dict[str, Any],
                      actual_results: Dict[str, Any]):
        """Compare two dictionaries and return a list of differences."""
        for key, value in expected_results.items():
            if key not in actual_results:
                self.comparison_results.append(
                    f"Key '{key}' is missing in actual results.")
                continue

            expected_value = value
            actual_value = actual_results[key]
            if isinstance(expected_value, dict) and isinstance(actual_value, dict):
                    self.compare_dicts(expected_value, actual_value)
            elif isinstance(expected_value, list) and isinstance(actual_value, list):
                self.comparison_results.extend(
                    self.compare_lists(expected_value, actual_value))
            elif expected_value != actual_value:
                self.comparison_results.append(
                    f"Value mismatch for key '{key}':"
                    f" expected '{expected_value}', got '{actual_value}'."
                )

        return self.comparison_results

    def compare_lists(self, expected_results: List[Any],
                      actual_results: List[Any]):
        """Compare two lists and return a list of differences."""
        for index, expected_value in enumerate(expected_results):
            if index >= len(actual_results):
                (self.comparison_results
                 .append(f"Index '{index}' is missing in actual results."))
                continue
            actual_value = actual_results[index]
            if (isinstance(expected_value, dict)
                    and isinstance(actual_value, dict)):
                self.comparison_results.extend(
                    self.compare_dicts(expected_value, actual_value))
            elif (isinstance(expected_value, list)
                  and isinstance(actual_value, list)):
                self.comparison_results.extend(
                    self.compare_lists(expected_value, actual_value))
            elif expected_value != actual_value:
                self.comparison_results.append(
                    f"Value mismatch at index '{index}':"
                    f" expected '{expected_value}', got '{actual_value}'."
                )

        return self.comparison_results

    def compare_values(self, expected_results: Any, actual_results: Any):
        """Compare two values and return a list of differences."""
        self.comparison_results = []

        if (isinstance(expected_results, dict)
                and isinstance(actual_results, dict)):
            return self.compare_dicts(expected_results, actual_results)
        elif (isinstance(expected_results, list)
              and isinstance(actual_results, list)):
            return self.compare_lists(expected_results, actual_results)
        else:
            if expected_results != actual_results:
                return [f"Value mismatch: expected '{expected_results}', "
                        f"got '{actual_results}'."]
            else:
                return []
