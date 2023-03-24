#create a file in /tmp.
file {'/tmp/school':
  ensure  => present,
  owner   => 'www-data',
  group   => 'ww-data',
  mode    => '0744',
  content => 'I love Puppet'
}
