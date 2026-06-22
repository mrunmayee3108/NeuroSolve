import signal

#HARDWARE FIREWALL
def timeout_handler(signum, frame):
    raise TimeoutError("Execution took too long!")

# SEMANTIC TRANSLATION LAYER 
def translate_error(error_obj):
    """Translates raw Python crashes into smart AI prompts."""
    if isinstance(error_obj, AssertionError):
        return f"LOGIC VIOLATION: You broke your own math invariant rule! Hint: {str(error_obj)}"
    elif isinstance(error_obj, TimeoutError):
        return "COMPUTATION HALTED: Your code got stuck in an infinite loop. Simplify the math."
    elif isinstance(error_obj, NameError):
        return f"VARIABLE ERROR: You tried to use a variable before defining it. Details: {str(error_obj)}"
    elif isinstance(error_obj, TypeError):
        return f"DATATYPE ERROR: You mixed up text and numbers. Details: {str(error_obj)}"
    else:
        return f"SYNTAX CRASH: {type(error_obj).__name__} - {str(error_obj)}. Check your code formatting."

# EXECUTION ENGINE
def execute_with_guardrails(ai_code):
    """Executes code securely and catches Ektu's semantic logic failures."""
    secure_locals = {}
    
   
    try:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(3)
    except AttributeError:
        pass 
    
    try:
        exec(ai_code, {"__builtins__": {}}, secure_locals)
        
        try: signal.alarm(0) 
        except AttributeError: pass
        
        return secure_locals.get('result', None), "Success"
        
    except Exception as e:
        try: signal.alarm(0)
        except AttributeError: pass
        
        
        smart_feedback = translate_error(e)
        return None, smart_feedback