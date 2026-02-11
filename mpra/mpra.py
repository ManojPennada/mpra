'''
*******************************************************************************
*IT'S OPENSOURCE ENJOY* 
SCRIPT NAME             : mpra.py
DESCRIPTION             : The `mpra` package offers a variety of utility
                          functions to manage files and directories, 
                          such as checking disk usage, organizing files 
                          by extension, monitoring directories, and more.
SCRIPT REV              : 1.0
SCRIPT DATE             : 2024-10-07
AUTHOR                  : Manoj Pennada, S K Prakalya
*******************************************************************************
'''


import os
import shutil
import time
import subprocess
import hashlib
import mimetypes
import stat
from datetime import datetime

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
    from openpyxl.utils import get_column_letter
    OPENPYXL_AVAILABLE = True
except ImportError:
    OPENPYXL_AVAILABLE = False

# Try to import PIL for image metadata
try:
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# Try to import mutagen for audio metadata
try:
    import mutagen
    from mutagen.mp3 import MP3
    from mutagen.flac import FLAC
    from mutagen.mp4 import MP4
    from mutagen.wave import WAVE
    MUTAGEN_AVAILABLE = True
except ImportError:
    MUTAGEN_AVAILABLE = False


# File categories mapping
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp', '.tiff', '.tif', '.psd', '.ai', '.eps', '.heic', '.heif', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.avif', '.raw', '.arw', '.cr2', '.crw', '.dng', '.nef', '.nrw', '.orf', '.rw2', '.rwl', '.srw', '.x3f'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp', '.3g2', '.mts', '.m2ts', '.ts', '.vob', '.f4v', '.asf', '.rm', '.rmvb', '.divx', '.ogv', '.m2v', '.mxf', '.mod', '.tod', '.dv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.alac', '.aiff', '.ape', '.dsf', '.dsd', '.opus', '.vorbis', '.ac3', '.eac3', '.dts', '.dtsma', '.dtshd', '.mka', '.oga'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.docm', '.dotx', '.odt', '.rtf', '.tex', '.latex', '.wps', '.pages', '.wpd', '.wp', '.wp5', '.wp6', '.mdown', '.markdown', '.rst', '.asciidoc'],
    'Spreadsheets': ['.xlsx', '.xls', '.csv', '.tsv', '.ods', '.xlsm', '.xltx', '.numbers', '.gnumeric', '.fods'],
    'Presentations': ['.ppt', '.pptx', '.odp', '.pptm', '.potx', '.key', '.keynote', '.fodp'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso', '.ace', '.xz', '.zst', '.lz4', '.lz', '.z', '.br', '.tbz', '.tbz2', '.tgz', '.tar.gz', '.tar.bz2', '.tar.xz', '.deb', '.rpm'],
    '3D Models': ['.obj', '.fbx', '.gltf', '.glb', '.blend', '.maya', '.ase', '.ply', '.stl', '.stp', '.step', '.iges', '.igs', '.usdz', '.usd', '.dae'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.fon', '.pfm', '.afm'],
    'Others': []
}


class Mpra:
    @staticmethod
    def disk_stats(directory_path):
        """Print total, used, and free disk space in GB."""
        directory_path = os.path.normpath(directory_path)
        try:
            total, used, free = shutil.disk_usage(directory_path)
            print(f"Total: {total // (2**30)} GB")
            print(f"Used: {used // (2**30)} GB")
            print(f"Free: {free // (2**30)} GB")
        except FileNotFoundError:
            print(f"Error: Directory {directory_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def organize_files(directory_path):
        """Organize files in the directory by extension."""
        directory_path = os.path.normpath(directory_path)
        if not os.path.exists(directory_path):
            print("Directory not found!")
            return

        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath):
                file_ext = filename.split('.')[-1]
                ext_dir = os.path.join(directory_path, file_ext)

                if not os.path.exists(ext_dir):
                    os.mkdir(ext_dir)

                shutil.move(filepath, os.path.join(ext_dir, filename))
        print("Files organized by extension.")

    @staticmethod
    def auto_categorize_files(directory_path):
        """Organize only uncategorized files into 'Others' folder. Directories and categorized files remain unchanged."""
        directory_path = os.path.normpath(directory_path)
        if not os.path.exists(directory_path):
            print("Directory not found!")
            return

        categorized_count = 0
        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)

            # Skip directories - keep them intact
            if os.path.isdir(filepath):
                continue

            if os.path.isfile(filepath):
                file_ext = os.path.splitext(filename)[1].lower()
                is_categorized = False

                # Check if file extension is in any category (except Others)
                for cat, extensions in FILE_CATEGORIES.items():
                    if cat != 'Others' and file_ext in extensions:
                        is_categorized = True
                        break

                # Only move files that are NOT in any category (uncategorized)
                if not is_categorized:
                    category_dir = os.path.join(directory_path, 'Others')
                    if not os.path.exists(category_dir):
                        os.mkdir(category_dir)

                    try:
                        shutil.move(filepath, os.path.join(
                            category_dir, filename))
                        categorized_count += 1
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")

        print(
            f"Uncategorized files moved to 'Others'! {categorized_count} files organized.")

    @staticmethod
    def monitor_directory(directory_path):
        """Monitor directory for new files."""
        directory_path = os.path.normpath(directory_path)
        if not os.path.exists(directory_path):
            print("Directory does not exist!")
            return

        print(f"Monitoring directory: {directory_path}")
        files_before = set(os.listdir(directory_path))
        try:
            while True:
                time.sleep(2)
                files_after = set(os.listdir(directory_path))
                new_files = files_after - files_before
                if new_files:
                    print(f"New files added: {', '.join(new_files)}")
                files_before = files_after
        except KeyboardInterrupt:
            print("Directory monitoring stopped.")

    @staticmethod
    def backup_files(src_directory, dest_directory):
        """Backup files from one directory to another."""
        src_directory = os.path.normpath(src_directory)
        dest_directory = os.path.normpath(dest_directory)
        if not os.path.exists(src_directory):
            print(f"Source directory {src_directory} does not exist.")
            return
        if not os.path.exists(dest_directory):
            os.makedirs(dest_directory)

        try:
            for filename in os.listdir(src_directory):
                src_file = os.path.join(src_directory, filename)
                dest_file = os.path.join(dest_directory, filename)
                shutil.copy2(src_file, dest_file)
            print(f"All files backed up to {dest_directory}")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def batch_rename(directory_path, prefix="", suffix=""):
        """Add a prefix or suffix to all file names in a directory."""
        directory_path = os.path.normpath(directory_path)
        if not os.path.exists(directory_path):
            print(f"Directory {directory_path} does not exist.")
            return

        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath):
                new_filename = f"{prefix}{filename}{suffix}"
                new_filepath = os.path.join(directory_path, new_filename)
                os.rename(filepath, new_filepath)
        print("All files renamed.")

    @staticmethod
    def run_command(command):
        """Run a system command."""
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Command failed: {e}")

    @staticmethod
    def delete_empty_dirs(directory_path):
        """Delete all empty subdirectories."""
        directory_path = os.path.normpath(directory_path)
        if not os.path.exists(directory_path):
            print("Directory not found!")
            return

        for dirpath, dirnames, filenames in os.walk(directory_path, topdown=False):
            if not dirnames and not filenames:
                os.rmdir(dirpath)
                print(f"Deleted empty directory: {dirpath}")
        print("Empty directories removed.")

    @staticmethod
    def filter_files_by_size(directory_path, min_size_bytes):
        """List all files larger than a given size in bytes."""
        directory_path = os.path.normpath(directory_path)
        if not os.path.exists(directory_path):
            print(f"Directory {directory_path} does not exist.")
            return

        large_files = []
        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath) and os.path.getsize(filepath) > min_size_bytes:
                large_files.append(filename)

        if large_files:
            print("Files larger than specified size:")
            for file in large_files:
                print(file)
        else:
            print("No files larger than the specified size.")

    @staticmethod
    def create_log(directory_path):
        """Generate a log file with the current date and time."""
        directory_path = os.path.normpath(directory_path)
        if not os.path.exists(directory_path):
            print(f"Directory {directory_path} does not exist.")
            return

        log_filename = os.path.join(directory_path, "logfile.txt")
        with open(log_filename, "a") as log_file:
            log_file.write(f"Log Entry at {
                           time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"Log file created at {log_filename}")

    @staticmethod
    def _format_size(size_bytes):
        """Convert bytes to human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"

    @staticmethod
    def _get_file_category(extension):
        """Get the category for a file extension."""
        ext_lower = extension.lower()
        for category, extensions in FILE_CATEGORIES.items():
            if ext_lower in extensions:
                return category
        return 'Others'

    @staticmethod
    def _get_file_hash(filepath, algorithm='md5'):
        """Calculate file hash (MD5 by default)."""
        try:
            hash_func = hashlib.new(algorithm)
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except:
            return ''

    @staticmethod
    def _get_file_attributes(filepath):
        """Get file attributes (Windows-specific attributes + general)."""
        attrs = []
        try:
            file_stat = os.stat(filepath)
            mode = file_stat.st_mode

            # Check if it's a symbolic link
            if os.path.islink(filepath):
                attrs.append('Symlink')

            # Windows-specific attributes
            if os.name == 'nt':
                import ctypes
                FILE_ATTRIBUTE_HIDDEN = 0x02
                FILE_ATTRIBUTE_SYSTEM = 0x04
                FILE_ATTRIBUTE_ARCHIVE = 0x20
                FILE_ATTRIBUTE_READONLY = 0x01

                file_attrs = ctypes.windll.kernel32.GetFileAttributesW(filepath)
                if file_attrs != -1:
                    if file_attrs & FILE_ATTRIBUTE_HIDDEN:
                        attrs.append('Hidden')
                    if file_attrs & FILE_ATTRIBUTE_SYSTEM:
                        attrs.append('System')
                    if file_attrs & FILE_ATTRIBUTE_ARCHIVE:
                        attrs.append('Archive')
                    if file_attrs & FILE_ATTRIBUTE_READONLY:
                        attrs.append('ReadOnly')
            else:
                # Unix permissions
                if not (mode & stat.S_IWUSR):
                    attrs.append('ReadOnly')

            return ', '.join(attrs) if attrs else 'Normal'
        except:
            return ''

    @staticmethod
    def _get_image_metadata(filepath):
        """Extract image metadata including EXIF data."""
        metadata = {
            'width': '', 'height': '', 'color_mode': '', 'dpi': '',
            'camera_make': '', 'camera_model': '', 'date_taken': '',
            'iso': '', 'aperture': '', 'shutter_speed': '', 'focal_length': '',
            'gps_latitude': '', 'gps_longitude': ''
        }

        if not PIL_AVAILABLE:
            return metadata

        try:
            with Image.open(filepath) as img:
                metadata['width'] = img.width
                metadata['height'] = img.height
                metadata['color_mode'] = img.mode

                # Get DPI
                if hasattr(img, 'info') and 'dpi' in img.info:
                    dpi = img.info['dpi']
                    metadata['dpi'] = f"{dpi[0]}x{dpi[1]}"

                # Get EXIF data
                exif_data = img._getexif() if hasattr(img, '_getexif') and img._getexif() else {}

                if exif_data:
                    for tag_id, value in exif_data.items():
                        tag = TAGS.get(tag_id, tag_id)

                        if tag == 'Make':
                            metadata['camera_make'] = str(value).strip()
                        elif tag == 'Model':
                            metadata['camera_model'] = str(value).strip()
                        elif tag == 'DateTimeOriginal':
                            metadata['date_taken'] = str(value)
                        elif tag == 'ISOSpeedRatings':
                            metadata['iso'] = str(value)
                        elif tag == 'FNumber':
                            if hasattr(value, 'numerator'):
                                metadata['aperture'] = f"f/{float(value):.1f}"
                            else:
                                metadata['aperture'] = f"f/{value}"
                        elif tag == 'ExposureTime':
                            if hasattr(value, 'numerator'):
                                if value < 1:
                                    metadata['shutter_speed'] = f"1/{int(1/float(value))}s"
                                else:
                                    metadata['shutter_speed'] = f"{float(value)}s"
                            else:
                                metadata['shutter_speed'] = str(value)
                        elif tag == 'FocalLength':
                            if hasattr(value, 'numerator'):
                                metadata['focal_length'] = f"{float(value):.1f}mm"
                            else:
                                metadata['focal_length'] = f"{value}mm"
                        elif tag == 'GPSInfo':
                            try:
                                gps_data = {}
                                for gps_tag_id, gps_value in value.items():
                                    gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                                    gps_data[gps_tag] = gps_value

                                if 'GPSLatitude' in gps_data and 'GPSLatitudeRef' in gps_data:
                                    lat = gps_data['GPSLatitude']
                                    lat_ref = gps_data['GPSLatitudeRef']
                                    lat_decimal = float(lat[0]) + float(lat[1])/60 + float(lat[2])/3600
                                    if lat_ref == 'S':
                                        lat_decimal = -lat_decimal
                                    metadata['gps_latitude'] = f"{lat_decimal:.6f}"

                                if 'GPSLongitude' in gps_data and 'GPSLongitudeRef' in gps_data:
                                    lon = gps_data['GPSLongitude']
                                    lon_ref = gps_data['GPSLongitudeRef']
                                    lon_decimal = float(lon[0]) + float(lon[1])/60 + float(lon[2])/3600
                                    if lon_ref == 'W':
                                        lon_decimal = -lon_decimal
                                    metadata['gps_longitude'] = f"{lon_decimal:.6f}"
                            except:
                                pass
        except:
            pass

        return metadata

    @staticmethod
    def _get_audio_metadata(filepath):
        """Extract audio file metadata."""
        metadata = {
            'duration': '', 'bitrate': '', 'sample_rate': '',
            'channels': '', 'artist': '', 'album': '', 'title': '', 'year': ''
        }

        if not MUTAGEN_AVAILABLE:
            return metadata

        try:
            ext = os.path.splitext(filepath)[1].lower()
            audio = None

            if ext == '.mp3':
                audio = MP3(filepath)
            elif ext == '.flac':
                audio = FLAC(filepath)
            elif ext in ['.m4a', '.mp4', '.m4b']:
                audio = MP4(filepath)
            elif ext == '.wav':
                audio = WAVE(filepath)
            else:
                audio = mutagen.File(filepath)

            if audio:
                # Duration
                if hasattr(audio, 'info') and hasattr(audio.info, 'length'):
                    duration_secs = int(audio.info.length)
                    mins, secs = divmod(duration_secs, 60)
                    hours, mins = divmod(mins, 60)
                    if hours > 0:
                        metadata['duration'] = f"{hours}:{mins:02d}:{secs:02d}"
                    else:
                        metadata['duration'] = f"{mins}:{secs:02d}"

                # Bitrate
                if hasattr(audio, 'info') and hasattr(audio.info, 'bitrate'):
                    metadata['bitrate'] = f"{audio.info.bitrate // 1000} kbps"

                # Sample rate
                if hasattr(audio, 'info') and hasattr(audio.info, 'sample_rate'):
                    metadata['sample_rate'] = f"{audio.info.sample_rate} Hz"

                # Channels
                if hasattr(audio, 'info') and hasattr(audio.info, 'channels'):
                    metadata['channels'] = str(audio.info.channels)

                # Tags
                if hasattr(audio, 'tags') and audio.tags:
                    tags = audio.tags
                    if hasattr(tags, 'get'):
                        metadata['artist'] = str(tags.get('artist', [''])[0]) if 'artist' in tags else ''
                        metadata['album'] = str(tags.get('album', [''])[0]) if 'album' in tags else ''
                        metadata['title'] = str(tags.get('title', [''])[0]) if 'title' in tags else ''
        except:
            pass

        return metadata

    @staticmethod
    def generate_file_report(directory_path, output_path=None, recursive=False):
        """
        Extract comprehensive metadata of all files in a directory and create a detailed Excel report.

        Args:
            directory_path: Path to the directory to scan
            output_path: Path for the output Excel file (default: directory_path/file_report.xlsx)
            recursive: If True, scan subdirectories as well (default: False)
        """
        if not OPENPYXL_AVAILABLE:
            print(
                "Error: openpyxl is required for this feature. Install it with: pip install openpyxl")
            return

        directory_path = os.path.normpath(directory_path)
        if not os.path.exists(directory_path):
            print(f"Directory {directory_path} does not exist.")
            return

        if output_path is None:
            output_path = os.path.join(directory_path, "file_report.xlsx")
        else:
            output_path = os.path.normpath(output_path)

        # Create workbook and worksheet
        wb = Workbook()
        ws = wb.active
        ws.title = "File Report"

        # Define styles
        header_font = Font(bold=True, color="FFFFFF", size=11)
        header_fill = PatternFill(
            start_color="4472C4", end_color="4472C4", fill_type="solid")
        header_alignment = Alignment(
            horizontal="center", vertical="center", wrap_text=True)
        link_font = Font(color="0563C1", underline="single")
        border = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin'),
            bottom=Side(style='thin')
        )

        # Define comprehensive headers
        headers = [
            "S.No", "File Name", "File Link", "Extension", "Category", "MIME Type",
            "Size", "Size (Bytes)", "Created Date", "Modified Date", "Accessed Date",
            "File Attributes", "MD5 Hash",
            # Image metadata
            "Width", "Height", "Color Mode", "DPI", 
            "Camera Make", "Camera Model", "Date Taken", "ISO", "Aperture", "Shutter Speed", "Focal Length",
            "GPS Latitude", "GPS Longitude",
            # Audio metadata
            "Duration", "Bitrate", "Sample Rate", "Channels", "Artist", "Album", "Title",
            # Path info
            "Full Path", "Parent Folder"
        ]

        # Write headers
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col, value=header)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_alignment
            cell.border = border

        # Collect files
        files_data = []
        if recursive:
            for root, dirs, files in os.walk(directory_path):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    files_data.append(filepath)
        else:
            for filename in os.listdir(directory_path):
                filepath = os.path.join(directory_path, filename)
                if os.path.isfile(filepath):
                    files_data.append(filepath)

        print(f"Processing {len(files_data)} files...")

        # Write file data
        for idx, filepath in enumerate(files_data, 1):
            try:
                stat_info = os.stat(filepath)
                filename = os.path.basename(filepath)
                extension = os.path.splitext(filename)[1]
                category = Mpra._get_file_category(extension)
                mime_type = mimetypes.guess_type(filepath)[0] or ''
                size_bytes = stat_info.st_size
                size_human = Mpra._format_size(size_bytes)
                created_date = datetime.fromtimestamp(
                    stat_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                modified_date = datetime.fromtimestamp(
                    stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                accessed_date = datetime.fromtimestamp(
                    stat_info.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                parent_folder = os.path.basename(os.path.dirname(filepath))

                # Get file attributes
                file_attrs = Mpra._get_file_attributes(filepath)

                # Get file hash (skip for very large files > 100MB to save time)
                file_hash = ''
                if size_bytes < 100 * 1024 * 1024:
                    file_hash = Mpra._get_file_hash(filepath)

                # Get image metadata if applicable
                img_meta = {'width': '', 'height': '', 'color_mode': '', 'dpi': '',
                           'camera_make': '', 'camera_model': '', 'date_taken': '',
                           'iso': '', 'aperture': '', 'shutter_speed': '', 'focal_length': '',
                           'gps_latitude': '', 'gps_longitude': ''}
                if category == 'Images':
                    img_meta = Mpra._get_image_metadata(filepath)

                # Get audio metadata if applicable
                audio_meta = {'duration': '', 'bitrate': '', 'sample_rate': '',
                             'channels': '', 'artist': '', 'album': '', 'title': ''}
                if category == 'Audio':
                    audio_meta = Mpra._get_audio_metadata(filepath)

                row = idx + 1  # +1 for header row
                col = 1

                # Basic info
                ws.cell(row=row, column=col, value=idx).border = border; col += 1
                ws.cell(row=row, column=col, value=filename).border = border; col += 1

                # File Link
                link_cell = ws.cell(row=row, column=col, value=filename)
                link_cell.hyperlink = filepath
                link_cell.font = link_font
                link_cell.border = border; col += 1

                ws.cell(row=row, column=col, value=extension).border = border; col += 1
                ws.cell(row=row, column=col, value=category).border = border; col += 1
                ws.cell(row=row, column=col, value=mime_type).border = border; col += 1
                ws.cell(row=row, column=col, value=size_human).border = border; col += 1
                ws.cell(row=row, column=col, value=size_bytes).border = border; col += 1
                ws.cell(row=row, column=col, value=created_date).border = border; col += 1
                ws.cell(row=row, column=col, value=modified_date).border = border; col += 1
                ws.cell(row=row, column=col, value=accessed_date).border = border; col += 1
                ws.cell(row=row, column=col, value=file_attrs).border = border; col += 1
                ws.cell(row=row, column=col, value=file_hash).border = border; col += 1

                # Image metadata
                ws.cell(row=row, column=col, value=img_meta.get('width', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('height', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('color_mode', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('dpi', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('camera_make', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('camera_model', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('date_taken', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('iso', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('aperture', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('shutter_speed', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('focal_length', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('gps_latitude', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=img_meta.get('gps_longitude', '')).border = border; col += 1

                # Audio metadata
                ws.cell(row=row, column=col, value=audio_meta.get('duration', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=audio_meta.get('bitrate', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=audio_meta.get('sample_rate', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=audio_meta.get('channels', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=audio_meta.get('artist', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=audio_meta.get('album', '')).border = border; col += 1
                ws.cell(row=row, column=col, value=audio_meta.get('title', '')).border = border; col += 1

                # Full Path (with hyperlink)
                path_cell = ws.cell(row=row, column=col, value=filepath)
                path_cell.hyperlink = filepath
                path_cell.font = link_font
                path_cell.border = border; col += 1

                ws.cell(row=row, column=col, value=parent_folder).border = border

                # Progress indicator every 100 files
                if idx % 100 == 0:
                    print(f"Processed {idx}/{len(files_data)} files...")

            except Exception as e:
                print(f"Error processing {filepath}: {e}")
                continue

        # Auto-adjust column widths
        column_widths = [
            6, 30, 30, 10, 12, 25,  # Basic info
            10, 12, 19, 19, 19,  # Size and dates
            15, 32,  # Attributes and hash
            8, 8, 10, 12,  # Image dimensions
            15, 20, 19, 8, 10, 12, 12,  # Image EXIF
            12, 12,  # GPS
            10, 12, 12, 10, 20, 20, 25,  # Audio
            50, 20  # Path info
        ]
        for col, width in enumerate(column_widths, 1):
            if col <= len(headers):
                ws.column_dimensions[get_column_letter(col)].width = width

        # Freeze header row
        ws.freeze_panes = 'A2'

        # Add summary sheet
        summary_ws = wb.create_sheet(title="Summary")
        summary_ws.cell(row=1, column=1, value="File Report Summary").font = Font(
            bold=True, size=14)
        summary_ws.cell(row=3, column=1,
                        value="Directory:").font = Font(bold=True)
        summary_ws.cell(row=3, column=2, value=directory_path)
        summary_ws.cell(row=4, column=1,
                        value="Total Files:").font = Font(bold=True)
        summary_ws.cell(row=4, column=2, value=len(files_data))
        summary_ws.cell(row=5, column=1,
                        value="Report Generated:").font = Font(bold=True)
        summary_ws.cell(row=5, column=2,
                        value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        summary_ws.cell(row=6, column=1,
                        value="Recursive Scan:").font = Font(bold=True)
        summary_ws.cell(row=6, column=2, value="Yes" if recursive else "No")
        
        # Optional packages info
        summary_ws.cell(row=8, column=1, value="Metadata Capabilities:").font = Font(bold=True, size=12)
        summary_ws.cell(row=9, column=1, value="PIL (Image EXIF):").font = Font(bold=True)
        summary_ws.cell(row=9, column=2, value="Available" if PIL_AVAILABLE else "Not installed (pip install Pillow)")
        summary_ws.cell(row=10, column=1, value="Mutagen (Audio):").font = Font(bold=True)
        summary_ws.cell(row=10, column=2, value="Available" if MUTAGEN_AVAILABLE else "Not installed (pip install mutagen)")

        # Category breakdown
        summary_ws.cell(row=12, column=1, value="Category Breakdown").font = Font(
            bold=True, size=12)
        category_counts = {}
        category_sizes = {}
        for filepath in files_data:
            try:
                ext = os.path.splitext(filepath)[1]
                cat = Mpra._get_file_category(ext)
                category_counts[cat] = category_counts.get(cat, 0) + 1
                category_sizes[cat] = category_sizes.get(
                    cat, 0) + os.path.getsize(filepath)
            except:
                pass

        row = 13
        summary_ws.cell(row=row, column=1,
                        value="Category").font = Font(bold=True)
        summary_ws.cell(row=row, column=2,
                        value="Count").font = Font(bold=True)
        summary_ws.cell(row=row, column=3,
                        value="Total Size").font = Font(bold=True)
        for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
            row += 1
            summary_ws.cell(row=row, column=1, value=cat)
            summary_ws.cell(row=row, column=2, value=count)
            summary_ws.cell(row=row, column=3, value=Mpra._format_size(
                category_sizes.get(cat, 0)))

        summary_ws.column_dimensions['A'].width = 25
        summary_ws.column_dimensions['B'].width = 50
        summary_ws.column_dimensions['C'].width = 15

        # Save workbook
        try:
            wb.save(output_path)
            print(f"\nFile report generated successfully: {output_path}")
            print(f"Total files processed: {len(files_data)}")
        except Exception as e:
            print(f"Error saving report: {e}")
