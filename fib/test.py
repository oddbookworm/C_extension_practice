try:
    import myModule
except ImportError:
    import fib.myModule

print(myModule.fib(10))