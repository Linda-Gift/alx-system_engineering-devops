# puppet manifest to change no of req.
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 3072'\n",
}