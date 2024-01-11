# 101-setup_web_static.pp

# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Create web_static directories
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => [File['/data/web_static'], File['/data/web_static/releases/test']],
}

# Create an HTML file
file { '/data/web_static/releases/test/index.html':
  content => '<html><head></head><body>Holberton School</body></html>',
  require => File['/data/web_static/releases/test'],
}

# Reload Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/data/web_static/current'],
}

