###Higher-Order Functions

**High-order function:** a function that takes a function as an argument value or a function that returns a function as a return value

**Applying a UDF:**
- create a new frame
- bind the formal parameters to arguments
- execute the body

**When a function is called:**

1. Add a local frame
2. Copy the parent of the function to the local frame
3. Bind the <formal parameters> to the aruments in the local frame
4. Execute the body of the function in the envrionment that starts with the local frame

**Local Names are not visible to Other (non-nested) functions**
- an environment is a sequence of frames
- the envrionemnt created by calling a top-level function (no def within def) consists of one local frame, followed by the global frame. 
