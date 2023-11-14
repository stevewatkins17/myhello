import FizzBuzz as fb

def test_getFizzBuzz():
    assert fb.getFizzBuzz(17) == 17
    assert fb.getFizzBuzz(10) == "Buzz"
    assert fb.getFizzBuzz(45) == "FizzBuzz"
    assert fb.getFizzBuzz(12) == "Fizz"
    assert fb.main(17) == 17

def test_main():
    assert fb.main(17) == 17

