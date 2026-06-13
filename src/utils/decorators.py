import inspect
import os

from utils.exceptions import UnauthorizedDirectoryError

def validate_tools_params(func):

    valids_working_dirs = os.getenv('ALLOWED_WORKING_DIRS','').split(',')

    def inner(*args, **kwargs):
        sig = inspect.signature(func)
        params = sig.bind(*args, **kwargs)
        params.apply_defaults()
        tool_args = dict(params.arguments)

        if 'working_dir' in tool_args and tool_args.get('working_dir') not in valids_working_dirs:
            raise UnauthorizedDirectoryError(f'Agente não tem permissão para acessar working_dir = {tool_args.get('working_dir')}')
        
        return func(*args)

    return inner

def error_to_string_handler(func):

    def inner(*args, **kwargs):
        try:
            return func(*args)
        except Exception as e:
            return f"Error: ao executar tool {func.__name__}: {repr(e)}"
        

    return inner