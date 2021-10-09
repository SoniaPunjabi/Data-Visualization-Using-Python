"""
Tests for functions written in data_visualization
"""
import pytest
import os
import sys
os.chdir("..")
my_path = os.getcwd()
sys.path.append(my_path)
os.chdir("test")
import src.data_visualization as dvi


def test_barchart():
    """
    Test to check if the BarChart.xlsl exists after the barchart function is executed
    """
    dvi.barchart([99, 55, 66], [65, 25, 85], [77, 88, 44], [999, 911, 922])
    assert os.path.isfile('./BarChart.xlsx')


def test_pie_chart():
    """
        Test to check if the PieChart.xlsl exists after the pie_chart function is executed
    """
    dvi.pie_chart([99, 55, 66], [65, 25, 85], [77, 88, 44], [999, 911, 922])
    assert os.path.isfile('./ PieChart.xlsx')


def test_bell_curve():
    """
    Test to check if the Bell_curve.xlsl exists after the bell_curve function is executed
    """
    dvi.bell_curve([99, 55, 66], [65, 25, 85], [77, 88, 44], [999, 911, 922])
    assert os.path.isfile('./Bell_curve.xlsx')


def test_overall_report():
    """
    Test to check if the Overall_Report.xlsl exists after the overall_report function is executed
    """
    dvi.overall_report([99, 55, 66], [65, 25, 85], [77, 88, 44], [999, 911, 922])
    assert os.path.isfile('./Overall_Report.xlsx')