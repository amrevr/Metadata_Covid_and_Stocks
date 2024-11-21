import os
import hashlib

def generate_sha256(file_path):
    """Generate SHA-256 checksum for a given file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def create_manifest(directory, manifest_file):
    """Create a manifest.txt file with checksums and file paths."""
    with open(manifest_file, 'w') as manifest:
        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                # Generate checksum
                checksum = generate_sha256(file_path)
                # Write to manifest with relative path
                relative_path = os.path.relpath(file_path, directory)
                manifest.write(f'SHA-256: {checksum}  {relative_path}\n')

if __name__ == "__main__":
    input_directory = "C:/Users/ender/SynologyDrive/RPI/csci4350 (data science)/Assignment 3/Dataset II (Mine) AIP"  # AIP directory
    output_manifest = os.path.join(input_directory, "manifest.txt")

    create_manifest(input_directory, output_manifest)
    print(f'Manifest created at: {output_manifest}')
