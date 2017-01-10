# Daemonizing celery for use with own process manager


 * Use the following link as an aid
   [https://hairycode.org/2013/07/23/first-steps-with-celery-how-to-not-trip/](https://hairycode.org/2013/07/23/first-steps-with-celery-how-to-not-trip/)
 * To start a worker from the command line anywhere use the following example
   ``` celery worker -A daemonized.worker.celery_worker -l debug ```

