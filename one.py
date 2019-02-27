#one.py


def func():
    print("Func() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print ('ONE.PY IS BEING RUN DIRECTLY!')
else:
    print ('ONE.PY HAS BEEN IMPORTED!')