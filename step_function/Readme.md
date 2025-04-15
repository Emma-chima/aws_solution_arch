☕ Tea-Making Workflow with AWS Step Functions
=============================================

🚀 Project Overview
-------------------

This mini project was designed as a hands-on way for me to learn and understand how **AWS Step Functions** work by simulating a real-world sequence — in this case, making a cup of tea.

The idea was to break the tea-making process into simple tasks, automate them using AWS Lambda, and orchestrate the entire flow with AWS Step Functions.

This isn't a complex or enterprise-level workflow just a simple experiment to grasp how state machines, tasks, roles, and Lambda functions integrate together.

🧠 Project Logic
----------------

The tea-making process was broken into 4 distinct steps:

1.  **Boil Water**
    
2.  **Add Tea Leaves**
    
3.  **Add Milk and Sugar**
    
4.  **Serve Tea**
    

Each step was mapped to a separate AWS Lambda function, and all four were orchestrated through a Step Functions state machine. Here’s how the flow was defined:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   textCopyEditBoilWater -> AddTeaLeaves -> AddMilkSugar -> ServeTea   `

🛠️ Technologies Used
---------------------

*   **AWS CloudFormation** – to define and deploy all resources as infrastructure-as-code
    
*   **AWS Lambda** – for each step in the tea-making process
    
*   **AWS Step Functions** – to manage the state machine and workflow
    
*   **IAM Roles & Policies** – to manage permissions between services
    
*   **AWS CLI** – for validation and manual operations
    
*   **YAML** – as the CloudFormation template format


⚙️ Key Concepts I Learned
-------------------------

*   **State Machine Logic:** How different states (tasks) can be connected in sequence
    
*   **Lambda Permissions:** IAM roles are required to allow Step Functions to invoke Lambda
    
*   **Inline Lambda Code:** You can define simple Lambda logic directly in CloudFormation
    
*   **Handler Configuration:** The handler value must match the inline function name, not the filename
    
*   **Debugging AWS Errors:** Interpreting and solving issues like Runtime.ImportModuleError

- The power of **Step Functions** to simplify coordination between services.
- How to use **CloudFormation** to automate deployments and avoid manual setup.
- The importance of proper **IAM roles and permissions** when working with AWS services.
- Debugging and testing small parts first is the key when working with multiple interconnected services.

---

## 🧗 Challenges Faced & Lessons Learned

- **Runtime.ImportModuleError**:  
  Initially got the error `No module named 'boil_water'` because I incorrectly set the Lambda handler as `boil_water.lambda_handler`. Since the functions were defined inline, the correct handler should have been simply `lambda_handler` or `index.lambda_handler` .

- **CloudFormation Role Validation Error**:  
  Used `!Ref LambdaRole` instead of `!GetAtt LambdaRole.Arn`, which led to a role format validation error. Resolved this by referencing the actual ARN using `!GetAtt`.

- **Confusion About Lambda & Step Functions Integration**:  
  I didn’t fully understand how Step Functions invoke Lambda functions, so I broke down the problem. I tested each Lambda function individually in the console first to be sure they worked before linking them in the state machine.

- **IAM Permission Confusion**:  
  Learned that the Step Function needs permission to invoke the Lambda functions, and each Lambda function must also have permission to write logs to CloudWatch. Defining correct IAM roles was crucial for everything to work.

---

## ✅ Result

After resolving the issues and properly setting permissions and handlers, the entire tea-making process worked successfully. It was executed using a Step Functions state machine from start to finish with output at every stage.

---

## 📁 Files

- `template.yaml` – Contains all resources including roles, Lambda functions (inline), and the Step Function definition.

---

## 🙌 Final Thoughts

Even though it’s a simple project, this helped me gain practical experience with orchestrating serverless workflows on AWS. I now feel more confident in using Step Functions and can see their value in automating complex workflows in the cloud.