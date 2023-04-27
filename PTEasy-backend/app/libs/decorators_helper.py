# from functools import wraps


# def paginate(view_func):
#     @wraps(view_func)
#     def wrapper(*args, **kwargs):
#         # Get pagination parameters from request
#         rq_data = request.args.to_dict()
#         page = int(rq_data.get('page', 1))
#         size = int(rq_data.get('size', 10))
#         offset = (page - 1) * size
#         # Call the original view function with additional pagination arguments
#         return view_func(*args, offset=offset, size=size, **kwargs)
#
#     # Preserve the original function's name
#     wrapper.__name__ = view_func.__name__
#     return wrapper