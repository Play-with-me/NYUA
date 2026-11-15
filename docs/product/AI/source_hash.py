"""Versioned text-source integrity; never use for binary/upstream artifact hashes."""
import hashlib

SOURCE_HASH_POLICY = 'utf8-text-bom-removed-universal-newlines-lf-v1'


def canonical_source_text(path):
    # Strict decoding; preserve every character/space except BOM and newline representation.
    return path.read_bytes().decode('utf-8-sig').replace('\r\n', '\n').replace('\r', '\n')


def source_sha256(path):
    return hashlib.sha256(canonical_source_text(path).encode('utf-8')).hexdigest()
