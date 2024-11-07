class Engine:
    def start(self):
        print("Engine is starting.")

    def stop(self):
        print("Engine is stopping.")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start_engine(self):
        self.engine.start()
    
    def stop_engine(self):
        self.engine.stop()

# Demonstration
car = Car()
car.start_engine()
car.stop_engine()