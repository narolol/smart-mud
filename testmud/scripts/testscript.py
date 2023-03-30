from evennia import DefaultScript
import openai
import os

class TestScript(DefaultScript):
    """
    This class defines the script itself

    """

    
    def at_script_creation(self):
        self.key = "testscript"
        self.desc = "Testando"
        self.interval = 10  # seconds
        # self.repeats = 5  # repeat only a certain number of times
        self.start_delay = False  # wait self.interval until first call
        # self.persistent = True
        api_key = os.environ["OPEN_API_KEY"]
        openai.api_key = api_key
        


        
    
    
    def at_repeat(self):
        """
        This gets called every self.interval seconds. We make
        a random check here so as to only return 33% of the time.
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who outputs witty and funny sentences about bodily functions and output it as a first person. Keep them short."},
                {"role": "user", "content": "Give me a funny sentence about bladder."}
            ],
            max_tokens=100,
            n=1,
            temperature=0.8,
        )
        
        self.obj.msg(response.choices[0].message['content'].strip())