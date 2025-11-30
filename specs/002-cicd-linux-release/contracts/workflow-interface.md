# Workflow Interface

## Trigger
- **Event**: `push`
- **Ref**: `refs/tags/v*`

## Inputs
- None (triggered by tag push)

## Outputs
- **Artifact**: `ddc-control` (Linux executable)
- **Release**: GitHub Release with tag name
