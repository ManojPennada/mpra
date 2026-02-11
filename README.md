# Multipurpose Resource Automation(MPRA) Package

## Overview

The `mpra` package offers a variety of utility functions to manage files and directories, such as checking disk usage, organizing files by extension, monitoring directories, and more.

## Features

<div class="function">
    <h3>Disk Usage Checker</h3>
    <p>
        <strong>Function:</strong> <code>disk_stats(directory_path)</code><br>
        <strong>Description:</strong> This function takes a directory path as input and returns the total, used, and free disk space in gigabytes.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The path of the directory to check.</li>
    </ul>
    <p><strong>Returns:</strong></p>
    <ul>
        <li>Total disk space, used space, and free space in gigabytes.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.disk_stats('/path/to/directory')</code></pre>
</div>

<div class="function">
    <h3>File Organizer</h3>
    <p>
        <strong>Function:</strong> <code>organize_files(directory_path)</code><br>
        <strong>Description:</strong> This function organizes files in the specified directory into subdirectories based on file extensions.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The path of the directory to organize.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.organize_files('/path/to/directory')</code></pre>
</div>

<div class="function">
    <h3>Auto Categorize Files</h3>
    <p>
        <strong>Function:</strong> <code>auto_categorize_files(directory_path)</code><br>
        <strong>Description:</strong> This function automatically organizes uncategorized files into an 'Others' folder. Files that match known categories (Images, Videos, Audio, Documents, Spreadsheets, Presentations, Archives, Data, 3D Models, Fonts) are left in place. Directories remain completely intact.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The path of the directory to auto-categorize.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.auto_categorize_files('/path/to/directory')</code></pre>
</div>

<div class="function">
    <h3>Directory Monitor</h3>
    <p>
        <strong>Function:</strong> <code>monitor_directory(directory_path)</code><br>
        <strong>Description:</strong> This function monitors a directory for new files and prints a message each time a new file is added.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The directory to monitor.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.monitor_directory('/path/to/directory')</code></pre>
</div>

<div class="function">
    <h3>File Backup</h3>
    <p>
        <strong>Function:</strong> <code>backup_files(source_directory, destination_directory)</code><br>
        <strong>Description:</strong> This function copies all files from the source directory to the destination directory.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>source_directory</code> (str): The path of the directory to copy files from.</li>
        <li><code>destination_directory</code> (str): The path of the directory to copy files to.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.backup_files('/source/directory', '/destination/directory')</code></pre>
</div>

<div class="function">
    <h3>Batch Rename Files</h3>
    <p>
        <strong>Function:</strong> <code>batch_rename(directory_path, prefix=None, suffix=None)</code><br>
        <strong>Description:</strong> This function renames all files in a directory by adding a prefix or suffix.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The path of the directory containing the files.</li>
        <li><code>prefix</code> (str, optional): The prefix to add to each file name.</li>
        <li><code>suffix</code> (str, optional): The suffix to add to each file name.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.batch_rename('/path/to/directory', prefix='backup_')</code></pre>
</div>

<div class="function">
    <h3>System Command Runner</h3>
    <p>
        <strong>Function:</strong> <code>run_command(command)</code><br>
        <strong>Description:</strong> This function takes a system command as input and executes it. It returns the command's output.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>command</code> (str): The system command to execute.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.run_command('ls -la')</code></pre>
</div>

<div class="function">
    <h3>Delete Empty Directories</h3>
    <p>
        <strong>Function:</strong> <code>delete_empty_dirs(directory_path)</code><br>
        <strong>Description:</strong> This function recursively searches through a directory and deletes all empty subdirectories.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The directory to clean up.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.delete_empty_dirs('/path/to/directory')</code></pre>
</div>

<div class="function">
    <h3>File Size Filter</h3>
    <p>
        <strong>Function:</strong> <code>filter_files_by_size(directory_path, min_size_bytes)</code><br>
        <strong>Description:</strong> This function lists all files in a directory that are larger than a specified size.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The path of the directory to search.</li>
        <li><code>min_size_bytes</code> (int): The minimum file size (in bytes) to filter.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.filter_files_by_size('/path/to/directory', min_size_bytes=1000000)</code></pre>
</div>

<div class="function">
    <h3>Log File Creator</h3>
    <p>
        <strong>Function:</strong> <code>create_log(directory_path)</code><br>
        <strong>Description:</strong> This function generates a log file in the specified directory, logging the current date and time each time the script runs.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The directory where the log file will be created.</li>
    </ul>
    <p><strong>Example:</strong></p>
    <pre><code>mpra.create_log('/path/to/directory')</code></pre>
</div>

<div class="function">
    <h3>Generate Comprehensive File Report</h3>
    <p>
        <strong>Function:</strong> <code>generate_file_report(directory_path, output_path=None, recursive=False)</code><br>
        <strong>Description:</strong> This function extracts comprehensive metadata from all files in a directory and generates a professional Excel report with detailed information including file properties, EXIF data, audio metadata, and more.
    </p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>directory_path</code> (str): The directory to scan for files.</li>
        <li><code>output_path</code> (str, optional): Path for the output Excel file. Default: <code>directory_path/file_report.xlsx</code></li>
        <li><code>recursive</code> (bool, optional): If True, scan subdirectories recursively. Default: False</li>
    </ul>
    <p><strong>Report Contents:</strong></p>
    <ul>
        <li><strong>File Report Sheet:</strong> 35+ columns including:
            <ul>
                <li>Basic Info: File name, extension, category, MIME type, size, dates, file attributes</li>
                <li>File Hash: MD5 hash for integrity checking and duplicate detection</li>
                <li>Image Metadata: Width, height, color mode, DPI (requires <code>Pillow</code>)</li>
                <li>EXIF Data: Camera make/model, date taken, ISO, aperture, shutter speed, focal length</li>
                <li>GPS Data: Latitude, longitude coordinates (extracted from EXIF)</li>
                <li>Audio Metadata: Duration, bitrate, sample rate, channels, artist, album, title (requires <code>mutagen</code>)</li>
                <li>Clickable hyperlinks to files and full paths</li>
            </ul>
        </li>
        <li><strong>Summary Sheet:</strong> Directory statistics, file count, category breakdown with counts and sizes</li>
    </ul>
    <p><strong>Examples:</strong></p>
    <pre><code>import mpra

# Generate report in the same directory
mpra.generate_file_report(r'C:\Users\Pictures')

# Custom output path
mpra.generate_file_report(r'C:\Users\Pictures', output_path=r'C:\Reports\my_report.xlsx')

# Include subdirectories
mpra.generate_file_report(r'D:\Data', recursive=True)</code></pre>
    
    <p><strong>Optional Dependencies for Full Metadata:</strong></p>
    <pre><code># For image EXIF data extraction
pip install Pillow

# For audio metadata extraction
pip install mutagen

# Or install both at once
pip install mpra[excel]</code></pre>
</div>

<footer>
    <p>&copy; 2024 MPRA Documentation. All rights reserved.</p>
</footer>

</body>
</html>

## Usage

```python
import mpra

# ===== Basic File Operations =====

# Check disk usage
mpra.disk_stats("/path/to/directory")

# Organize files by extension (.jpg, .txt, .pdf, etc.)
mpra.organize_files("/path/to/directory")

# Auto-categorize uncategorized files only (leaves known categories intact)
mpra.auto_categorize_files("/path/to/directory")

# ===== Directory Monitoring =====

# Monitor directory for new files
mpra.monitor_directory("/path/to/directory")

# ===== File Management =====

# Backup files
mpra.backup_files("/source", "/destination")

# Batch rename files with prefix/suffix
mpra.batch_rename("/path/to/directory", prefix="backup_")

# Delete empty subdirectories
mpra.delete_empty_dirs("/path/to/directory")

# Filter files by size (list files larger than 1MB)
mpra.filter_files_by_size("/path/to/directory", min_size_bytes=1000000)

# Create a log file in directory
mpra.create_log("/path/to/directory")

# ===== Advanced: Generate Comprehensive File Report =====

# Generate Excel report with all file metadata
mpra.generate_file_report(r"C:\Users\Pictures")

# Generate with custom output path
mpra.generate_file_report(r"C:\Data", output_path=r"C:\Reports\report.xlsx")

# Include subdirectories in the scan
mpra.generate_file_report(r"D:\Projects", recursive=True)

# Run a system command
mpra.run_command("dir /s")
```

## Installation

```bash
# Basic installation
pip install mpra

# With Excel report support
pip install mpra[excel]

# With full metadata extraction (images and audio)
pip install openpyxl Pillow mutagen
```

## File Categories

The `auto_categorize_files()` function supports these categories:

- **Images**: JPG, PNG, GIF, BMP, SVG, WEBP, HEIC, RAW, PSD, AI, EPS, AVIF, and 20+ more
- **Videos**: MP4, AVI, MKV, MOV, FLV, WMV, WEBM, 3GP, MTS, and more
- **Audio**: MP3, WAV, FLAC, AAC, OGG, WMA, M4A, OPUS, DSD, and more
- **Documents**: PDF, DOC, DOCX, TXT, RTF, ODT, LaTeX, Markdown, and more
- **Spreadsheets**: XLSX, XLS, CSV, TSV, ODS, NUMBERS
- **Presentations**: PPT, PPTX, ODP, KEY
- **Archives**: ZIP, RAR, 7Z, TAR, GZ, BZ2, ISO, XZ, and more
- **Data**: JSON, XML, YAML, TOML, SQL, SQLite, Parquet, HDF5, and more
- **3D Models**: OBJ, FBX, GLTF, BLEND, STL, STEP, IGES, USDZ, and more
- **Fonts**: TTF, OTF, WOFF, EOT, PFM, and more
- **Others**: Any unrecognized file types

## Requirements

- Python 3.6+
- openpyxl (for Excel report generation)
- Pillow (optional, for image EXIF metadata extraction)
- mutagen (optional, for audio metadata extraction)

