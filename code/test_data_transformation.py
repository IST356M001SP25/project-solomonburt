# tests/test_data_transformation.py
import unittest
import pandas as pd
from data_transformation import transform_air_quality_data

class TestDataTransformation(unittest.TestCase):

    def test_transform_air_quality_data(self):
        # Create a sample DataFrame
        raw_data = {
            'time': ['2025-05-10T00:00', '2025-05-10T01:00'],
            'carbon_monoxide': [0.1, 0.2],
            'nitrogen_dioxide': [10.5, 12.1]
        }
        raw_df = pd.DataFrame(raw_data)
        raw_df['time'] = pd.to_datetime(raw_df['time'])

        # Expected transformed DataFrame
        expected_data = {
            'time': ['2025-05-10T00:00', '2025-05-10T01:00', '2025-05-10T00:00', '2025-05-10T01:00'],
            'pollutant': ['carbon_monoxide', 'carbon_monoxide', 'nitrogen_dioxide', 'nitrogen_dioxide'],
            'value': [0.1, 0.2, 10.5, 12.1]
        }
        expected_df = pd.DataFrame(expected_data)
        expected_df['time'] = pd.to_datetime(expected_df['time'])

        # Perform the transformation
        transformed_df = transform_air_quality_data(raw_df.copy()) # Use a copy to avoid modifying the original

        # Assert that the transformed DataFrame is as expected
        pd.testing.assert_frame_equal(transformed_df, expected_df)

    def test_transform_air_quality_data_empty(self):
        # Test with an empty DataFrame
        empty_df = pd.DataFrame()
        transformed_df = transform_air_quality_data(empty_df)
        self.assertTrue(transformed_df.empty)

    def test_transform_air_quality_data_none(self):
        # Test with None input
        transformed_df = transform_air_quality_data(None)
        self.assertIsNone(transformed_df)

if __name__ == '__main__':
    unittest.main()