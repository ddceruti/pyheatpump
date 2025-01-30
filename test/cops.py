from pyheatpump import cop

def test_conventional():
    c = cop.calculate(source_temperature=20,
                  sink_temperature=60)
    assert c == 3.9818979919549604

def test_high_temperature():
    c = cop.calculate(source_temperature=100,
                  sink_temperature=155)
    assert c == 3.288629696394147

def test_carnot():
    c = cop.calculate(source_temperature=-20,
                      sink_temperature=170)
    assert c == 0.9329473684210527
