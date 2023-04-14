from datetime import datetime
from random import randint, choice

from app.models.FileInfo import FileInfo


def generate_random_filename():
    prefix = 'file_'
    suffix = randint(10000, 99999)
    return f"{prefix}{suffix}"


def generate_random_filetype():
    file_types = ['txt', 'jpg', 'png', 'pdf', 'docx', 'xlsx']
    return choice(file_types)


def generate_random_softpath():
    level = randint(1, 5)
    return "/".join([generate_random_filename() for _ in range(level)])


def insert_test_data(num_records=100):
    for _ in range(num_records):
        file_info = {
            'soft_path': generate_random_softpath(),
            'file_name': generate_random_filename(),
            'file_size': randint(1024, 10485760),  # 文件大小范围：1KB - 10MB
            'visit_time': int(datetime.now().timestamp()),
            'modify_time': int(datetime.now().timestamp()),
            'file_id': randint(1, 1000),
            'parent_id': randint(1, 100),
            'file_type': generate_random_filetype(),
            'is_delete': choice([0, 1])
        }
        FileInfo.create(file_info)


def test_get():
    # 获取主键为1的记录
    record = FileInfo.get(1)
    if record:
        print("Get record by primary key 1:")
        print(record['soft_path'], record['file_name'])
    else:
        print("No record found with primary key 1")


def test_filter_query():
    # 查询文件类型为'jpg'的记录
    filter_func = FileInfo.create_filter_func(FileInfo.file_type == 'jpg')
    jpg_files = FileInfo.query(filter_func).all()

    print("JPG files:")
    for file in jpg_files:
        print(file.soft_path, file.file_name)


def test_update():
    # 更新主键为1的记录的文件名
    new_file_name = "updated_file_name.txt"
    filter_func = FileInfo.create_filter_func(FileInfo.id == 1)
    FileInfo.update(filter_func, {'file_name': new_file_name})

    # 验证更新是否成功
    updated_record = FileInfo.get(1)
    if updated_record and updated_record['file_name'] == new_file_name:
        print("Update successful")
    else:
        print("Update failed")


def test_bulk_update():
    # 将所有文件大小小于10000的记录的is_delete字段设置为1
    filter_func = FileInfo.create_filter_func(FileInfo.file_size < 10000)
    FileInfo.bulk_update(filter_func, [{'is_delete': 1}])

    # 验证批量更新是否成功
    small_files = FileInfo.query(filter_func).all()
    if all(file.is_delete == 1 for file in small_files):
        print("Bulk update successful")
    else:
        print("Bulk update failed")


def test_delete():
    # 删除主键为1的记录
    FileInfo.delete(1)

    # 验证删除是否成功
    deleted_record = FileInfo.get(1)
    if not deleted_record:
        print("Delete successful")
    else:
        print("Delete failed")


def test_create():
    # 创建一条新记录
    new_file_info = {
        'soft_path': generate_random_softpath(),
        'file_name': generate_random_filename(),
        'file_size': randint(1024, 10485760),
        'visit_time': int(datetime.now().timestamp()),
        'modify_time': int(datetime.now().timestamp()),
        'file_id': randint(1, 1000),
        'parent_id': randint(1, 100),
        'file_type': generate_random_filetype(),
        'is_delete': choice([0, 1])
    }
    FileInfo.create(new_file_info)

    # 验证新记录是否成功创建
    filter_func = FileInfo.create_filter_func(
        FileInfo.soft_path == new_file_info['soft_path'],
        FileInfo.file_name == new_file_info['file_name']
    )
    created_record = FileInfo.query(filter_func).first()
    if created_record:
        print("Create successful")
    else:
        print("Create failed")


if __name__ == '__main__':
    # 确保表存在
    FileInfo._ensure_table_exists(force=True)
    # # 插入测试数据
    insert_test_data()

    # 执行测试
    test_get()
    test_filter_query()
    test_update()
    test_bulk_update()
    test_delete()
    test_create()
