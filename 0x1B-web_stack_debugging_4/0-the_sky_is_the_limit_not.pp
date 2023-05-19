# puppet manifest to change no of req.
$filename = '/etc/default/nginx'
$ulimit_value = '3072'

file { $filename:
  ensure  => file,
  content => "ULIMIT='-n ${ulimit_value}'\n",
}

# URL encode the file path for linting
$encoded_filename = URI.encode_www_form_component($filename)
exec { 'puppet_lint':
  command => "puppet lint ${encoded_filename}",
  path    => '/usr/bin',
  unless  => "puppet-lint ${encoded_filename}",
}
