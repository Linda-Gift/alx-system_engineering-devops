#puppet manifest to modify the num of requests made to nginx
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 3072'\n",
}
