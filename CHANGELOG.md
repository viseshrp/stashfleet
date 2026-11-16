# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.0.2] - <Unreleased>

### Added

-

### Changed

-

### Deprecated

-

### Removed

-

### Fixed

-

## Security

-

## [0.0.1] - 2026-11-15

### Added

- Initial PyPI release of `stashfleet`.
- Parallel server-to-client folder backups via `rclone` over OpenSSH/SFTP (`stashfleet run`).
- Streaming, cooperatively cancellable ZIP64 archive creation (`deflate`, `store`, `bzip2`, `lzma`) with atomic publication and SHA-256 verification.
- Optional cloud upload and checksum-verified upload retries without re-pulling source servers (`stashfleet retry-upload`).
- Explicit local and cloud backup retention pruning for managed completed runs.
- Offline configuration/dependency validation (`stashfleet doctor`), execution plan preview (`--dry-run`), local run history (`stashfleet status`), and zero-network local fixture demo (`stashfleet demo`).
