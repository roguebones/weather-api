class { 'python' :
  ensure      => 'present',
  version     => 'rh-python36-python',
  dev         => 'present',
  virtualenv  => 'present',
}