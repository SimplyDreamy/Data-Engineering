-----------
    Goal
-----------
Clean up problem left from Day 1 where my automated script couldn't find the file
Learn a bit of Docker so I can run the GitHub Action workflow before uploading to cloud



I then moved on to build a basic ETL pipeline pandas to process a raw global weather dataset.

I implemented data extraction from CSV, performed data cleaning including handling missing values, duplicate removal,
and text normalization, and enforced data types for consistency (apparently, you will run into problems if u don't).

I also encountered a data quality issue such as different missing data percentages and realized that
different percentages handling strategies depending on their sufficiency.

Finally, I saved the cleaned dataset for my future planned streamlit app.

-------------------------------
    Roadblocks & Debugging
-------------------------------
The first problem in the morning was that
My automated bot to run my Day 1 code was erroring, so I had to fix it up
I decided to use docker to make sure I wasn't making any silly mistakes as I heard other devs used it
and ran into a problem with the firewall from getting docker to work.

For some reason, it didn't appear on the app list, so I had to dig it out manually
After that, I ran a test, but it wasn't able to because It wasn't connected to GitHub

But since I was so just tired of setting things up, I just wrote --pull=false to continue without uploading



a big time waster was that even though I had a list of concepts in front of me that I plan to study by today,
I was still confused on what to do and felt overwhelmed by the terminology when I dug deeper
into the ETF workflow, and encountered terms such as profiling, quality, and EDA

So, I just built something simple instead