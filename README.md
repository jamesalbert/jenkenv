# jenkenv

Virtualenvs for jenkinsfile-runner

```sh
Usage:
  jenkenv list
  jenkenv run <jenkinsfile> [<version>]
  jenkenv run-jenkins [<version>]
  jenkenv use (local|global) <version>
  jenkenv clean [<version>]
  jenkenv install (-l|<version>)
  jenkenv uninstall <version>
  jenkenv (-h | --help)
  jenkenv --version

Options:
  -h --help     Show this screen.
  --version     Show version.
```

## Overview

This tool uses a pre-built release of [kohsuke/jenkinsfile-runner](https://github.com/kohsuke/jenkinsfile-runner). It provides a set of commands that make it easy to test your code with Jenkins without jumping through the usual hoops. You can either set your preferred Jenkins version local to your project, or globally as a default. To get started:

```
pip install jenkenv
```

Once installed, if you don't know the version you want to use, run: `jenkenv install -l` or:

```sh
jenkenv install 2.121.3
jenkenv use local 2.121.3
```

Now you'll want to install your plugins. Just run: `jenkenv run-jenkins`. The administrator password will output to stdout.

If we have a `Jenkinsfile` like:

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Hello world!'
            }
        }
    }
}
```

We can expect the output of `jenkenv run Jenkinsfile` to be:

```sh
Started
Running in Durability level: PERFORMANCE_OPTIMIZED
[Pipeline] node
Running on Jenkins in /var/folders/j6/j58qnzlj5j146_0q55660q300000gn/T/jenkinsTests.tmp/jenkins4609194858906807076test/workspace/job
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] echo
Hello world!
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```

All output pipes to stdout and `jenkenv` will exit with the build's status.

## Reference


`jenkenv list`

List installed versions. => denotes the local version, * denotes global

`jenkenv run <jenkinsfile> [<version>]`

- `<jenkinsfile>`: path to target Jenkinsfile
- `[<version>]`: optional version if local or global version is set; required otherwise.

Run the given Jenkinsfile through jenkinsfile-runner.

`jenkenv run-jenkins [<version>]`

- `[<version>]`: optional version if local or global version is set; required otherwise.

Run Jenkins serving at [http://localhost:8080](http://localhost:8080). You'll want to do this and install your desired plugins first before running `jenkenv run ...`.

`jenkenv use (local|global) <version>`

- `(local|global)`: If local is set, `.jenkins_version` will be created in your current directory. If global is set, `~/.jenkins_version` will be created and used when `./.jenkins_version` isn't present.
- `[<version>]`: optional version if local or global version is set; required otherwise.

Select the version of Jenkins you want to use.

`jenkenv clean [<version>]`

- `[<version>]`: optional version if local or global version is set; required otherwise.

Clears out `~/.jenkenv/<version>/jenkins_home`. Useful when you want to restart the plugin process without re-installing.

`jenkenv install (-l|<version>)`

- `-l`: list install-able versions.
- `<version>`: version to install

Either list all install-able versions or install the specified version.

`jenkenv uninstall <version>`

- `<version>`: version to uninstall

Uninstall the specified version.
