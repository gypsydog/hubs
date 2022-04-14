Hello there!

To run the project, you should run the following from the project folder:

...

    python3 -m venv ../hubs_venv
    
    source ../hubs_venv/bin/activate

    pip3 install -r requirements.txt

    py.test  --alluredir=allure-report ./test_hubs.py 
    
    allure serve allure-report



My automation task description was:
> Test automation
> 
> Write an automated test to check model uploading on https://www.hubs.com/manufacture/ using Python 3.7 (or any latest version) and PyTest
>
>Please submit the test(s) in Pull Request on https://github.com/3DHubs/3dhubs-qa-challenge/pulls
> 
> In case you have any questions feel free to reach out to roman.iutsis@hubs.com or let me know.

I've decided to implement API tests for that as they are much faster and usually take much less time for support and adopting changes than UI ones. Besides, API changes less often than UI usually.

Later on, I've contacted Roman on some tech questions and found out that Selenium was supposed to be used for the challenge, but I've already done the most difficult part - work flow investigation. 
I've got Roman approval on completing task with API tests approach.

About my project:
I've tried to make it compact but ready for extending with new testcases on other methods as well as framework functionality.
But still there are some things I would change in it if it was used as a part of testing process:

* Add some checkers for making sure, models have been uploaded OK: trying to get model back or at least some data about it and compare it to the expected values. I have not quite understood how to get the uploaded model data. Let's discuss it on review.
* Add response json validation against model or schema. But it's better to use model generation here, not to have to update large and complicated jsons by hand.
* Improve signing-in: Sometimes, I get 'Too many sign in attempts.Please try again later.' error if I run tests too often. Roman pointed out that this must be a bug with some cache flushing.
* Improve logging with cUrl generation: it's great for reproducing test scenarios by hand.
* Improve logging with more structured log: current solution is sufficient for the challenge. I guess using more advanced logger would be over-engineering. Still effective logging is a great value for a testing project.
* Add other technologies into parametrization - only 'cnc-machining', 'sheet-metal' are available for me, I guess at least 'FDM' is available in other countries.
* Further improvements of the project will require project structure complification.

I liked working on the task, solving issues and digging out the API with no description provided :)
Hope my work fits the requirements, and I'll have a chance to discuss it with the team. 
