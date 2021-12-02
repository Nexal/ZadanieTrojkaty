import pytest
import triangleType
import sys


class TestGetTriangleTypeFromLengths():
    @pytest.mark.parametrize("test_input,expected",[
        ([2, 3, 4], "scalene"),
        ([sys.maxsize, sys.maxsize-1, sys.maxsize-2], "scalene"),
        ([100, 99, 101], "scalene"),
        ([2, 2, 3], "isosceles"),
        ([sys.maxsize, sys.maxsize-1, sys.maxsize], "isosceles"),
        ([19997, 9999, 9999], "isosceles"),
        ([sys.maxsize, sys.maxsize, sys.maxsize], "equilateral"),
        ([1,1,1], "equilateral"),
        ([10, 10, 10], "equilateral"),
    ])
    def testHappyPath(self, test_input, expected):
        assert triangleType.getTriangleTypeFromLengths(test_input[0], test_input[1], test_input[2]) == expected

    @pytest.mark.parametrize("test_input", [
        (['1', 10, 10]),
        ([1, '', 10]),
        ([1, 3, 4.6]),
        ([None, 3, 4.6]),
        ([6, [1,4], 4.6]),
    ])
    def testIncorrectType(self, test_input):
        with pytest.raises(TypeError):
            triangleType.getTriangleTypeFromLengths(test_input[0], test_input[1], test_input[2])

    @pytest.mark.parametrize("test_input", [
        ([0,1,2]),
        ([6, -1, 10]),
        ([1, 3, -sys.maxsize]),
    ])
    def testIncorrectValue(self, test_input):
        with pytest.raises(ValueError):
            triangleType.getTriangleTypeFromLengths(test_input[0], test_input[1], test_input[2])

    @pytest.mark.parametrize("test_input", [
        ([1,2,3]),
        ([500, 1001, 500]),
        ([int(sys.maxsize/2) - 1, int(sys.maxsize/2) - 1, sys.maxsize]),
    ])
    def testImpossibleTriangle(self, test_input):
        with pytest.raises(ValueError):
            triangleType.getTriangleTypeFromLengths(test_input[0], test_input[1], test_input[2])
