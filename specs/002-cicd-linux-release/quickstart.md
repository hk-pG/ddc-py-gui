# Quickstart: Creating a Release

To create a new release for Linux:

1.  **Commit your changes**: Ensure all changes are committed and pushed to the main branch.
2.  **Tag the commit**: Create a new tag following the version pattern `vX.Y.Z`.
    ```bash
    git tag v1.0.0
    ```
3.  **Push the tag**:
    ```bash
    git push origin v1.0.0
    ```
4.  **Monitor the Workflow**: Go to the "Actions" tab in the GitHub repository to see the "Build and Release" workflow running.
5.  **Verify Release**: Once the workflow completes, go to the "Releases" section to find the new release with the `ddc-control` executable attached.
