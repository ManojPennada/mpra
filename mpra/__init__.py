from .mpra import Mpra, FILE_CATEGORIES

# Expose all methods at package level for easy import
disk_stats = Mpra.disk_stats
organize_files = Mpra.organize_files
auto_categorize_files = Mpra.auto_categorize_files
monitor_directory = Mpra.monitor_directory
backup_files = Mpra.backup_files
batch_rename = Mpra.batch_rename
run_command = Mpra.run_command
delete_empty_dirs = Mpra.delete_empty_dirs
filter_files_by_size = Mpra.filter_files_by_size
create_log = Mpra.create_log
generate_file_report = Mpra.generate_file_report

__all__ = [
    'disk_stats',
    'organize_files',
    'auto_categorize_files',
    'monitor_directory',
    'backup_files',
    'batch_rename',
    'run_command',
    'delete_empty_dirs',
    'filter_files_by_size',
    'create_log',
    'generate_file_report',
    'FILE_CATEGORIES',
    'Mpra'
]
