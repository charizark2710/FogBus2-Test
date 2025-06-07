from pprint import pformat
from .base import ApplicationUserSide
from ...component.basic import BasicComponent
from time import sleep

class FibonacciDemo1(ApplicationUserSide):

    def __init__(
            self,
            videoPath: str,
            targetHeight: int,
            showWindow: bool,
            fibonacci_size: int,
            basicComponent: BasicComponent):
        super().__init__(
            appName='FibonacciDemo1',
            videoPath=videoPath,
            targetHeight=targetHeight,
            showWindow=showWindow,
            fibonacci_size=fibonacci_size,
            basicComponent=basicComponent)

    def prepare(self):
        pass

    def _run(self):
        self.basicComponent.debugLogger.info(
            'Application is running: %s', self.appName)

        inputData = {
            'n': self.fibonacci_size,
        }

        # put it in to data uploading queue
        while True:            
            self.dataToSubmit.put(inputData)
            self.basicComponent.debugLogger.info(
                'Data has sent n: %.2f', 70000)
            result = self.resultForActuator.get()
            print(f"Size of result: {len(result)}")
            # check type of result and print it out
            result_type = type(result)
            print(f"Type of result: {result_type}")
            self.basicComponent.debugLogger.info('Received results: \r\n%s', result)
            self.basicComponent.debugLogger.info('Done with FibonacciDemo1')
            sleep(5)
