#A puppet manifest to change num of req. made to nginx
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 4096'\n",
}
