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

<footer>
    <p>&copy; 2024 MPRA Documentation. All rights reserved.</p>
</footer>

</body>
</html>


## Usage

```python
from mpra import mpra

mpra.disk_stats("/path/to/directory")
mpra.organize_files("/path/to/directory")
```
