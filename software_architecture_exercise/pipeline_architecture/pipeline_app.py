class NumberPipeline:
    def __init__(self):
        self.data = []

    def stage1(self): # generate numbers
        self.data = list(range(1, 101))

    def stage2(self): # filter even numbers
        for num in self.data:
            if num % 2 != 0:
                self.data.remove(num)

    def stage3(self): # square numbers
        for i in range(len(self.data)):
            self.data[i] = self.data[i] ** 2

    def stage4(self): # output results
        print("Processed Numbers:", self.data)

    def run_pipeline(self): # run all stages
        self.stage1()
        self.stage2()
        self.stage3()
        self.stage4()

pipeline = NumberPipeline()
pipeline.run_pipeline()
