# Creates a file in /tmp with specified permissions, owner, group, and content

file {'/tmp/school':
  ensure  => present,
  owner   => 'www-data',
  group   => 'ww-data',
  mode    => '0744',
  content => 'I love Puppet'
}
