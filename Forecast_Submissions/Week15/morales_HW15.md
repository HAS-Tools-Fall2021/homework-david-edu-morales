# David Morales, 12/02/21, HW15

### Rationale:

1. According to the *slurm* output file, I used the following resources: 
   
   > This job is allocated 1 node(s), 1 core(s)/node and 5 Gigabytes of memory

    I'm not sure how long I needed to wait on the queue, but it was no longer than two minutes. I also did not refresh when the status showed "running" so my script must have been very quick. I tried following the hyperlink provided at the bottom of the slurm2690060.out file to check for more details but after logging in, it couldn't find the job referenced.

2. The most confusing part about setting up the job was the importance of the two lines of code:
   
   ```
   module load python
   source ~/mypyenv/bin/activate
   ```
   It is not quite clear to me why this needed to be reincorporated into the run_python.sh file after we had already incorporated it into the shell. As far as the confusing part regardng running the job, it was actually very straightforward once we got it set up as a classroom. It was difficult for me to run the Jupyter Notebook interactively through OnDemand, however that wasn't done through Puma.
   
3. I don't have a lot of questions regarding the homework assignment, however I am interested in parallel computing, regardless of whether I think I will need it for my thesis work or not.



