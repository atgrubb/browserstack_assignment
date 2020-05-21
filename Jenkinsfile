properties([pipelineTriggers([githubPush()])])

node {
    git url: 'https://github.com/atgrubb/browserstack_assignment.git', branch: 'master'
    docker.image('joyzoursky/python-chromedriver').inside {
        sh 'pip install selenium'
        sh 'pip install pytest'
        sh 'pip install pytest-xdist'
        sh 'rm -fr browserstack_assignment'
        sh 'git clone https://github.com/atgrubb/browserstack_assignment.git'
        sh 'cd browserstack_assignment && py.test --browser chrome --browser-version 81 --browser-stack-enabled True -n 5'
    }
}