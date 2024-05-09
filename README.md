# EXTEND
EMR Numerical Data Extraction Tool

The "EXTEND" tool, short for "Extraction of EMR Numerical Data," offers a flexible natural language processing (NLP) solution tailored for the precise extraction of clinical numeric parameters. Continuously enriching its dictionary and incorporating new rules, EXTEND can be readily adapted to capture additional numerical data crucial for clinical outcomes research.

I now developed an interface to better haddling setting up parameters, monitoring the processes.

For more details, please refer to the publication:
        https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6858776/
        
Citation:
Cai, T., Zhang, L., Yang, N., Kumamaru, K.K., Rybicki, F.J., Cai, T. and Liao, K.P., 2019. EXTraction of EMR numerical data: an efficient and             generalizable tool to EXTEND clinical research. BMC medical informatics and decision making, 19, pp.1-7.

Please note that due to file size restrictions, the full version of the tool can be obtained by emailing Tianrun Cai at tcai1@bwh.harvard.edu.

Prerequisite: 
1.	    Sign up at www.enrichfuture.org using your academic email.
2.	    Operating system requirement: Windows 8 or later, with a minimum of 8GB RAM.
3.	    Ensure data is stored in an MSSQL database with a minimum of 5 columns: patient ID, Note ID, Note date, Note type, and Note.
   
To begin using:

4.	    Set the environment variable ‘EXTEND_HOME’ to the path of the main Extend folder.
5.	    Provide your username and registered email address within the settings panel.
6.	    Input and validate MSSQL connection details by clicking the ‘Test Server’ button.
7.	    Specify the table name and required column names. Validate entries with the ‘Test Query’ button.
8.	    Within the main panel, enter the project name and the range of patient IDs.
9.	    Initiate the process by selecting the ‘Run’ button.
10.         Verify the outcomes in the 'results' directory located within the primary Extend pathway.



