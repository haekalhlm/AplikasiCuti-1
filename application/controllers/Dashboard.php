<?php
defined('BASEPATH') or exit('No direct script access allowed');

class Dashboard extends CI_Controller
{
    public function __construct()
    {
        parent::__construct();
       
    }

    public function index()
    {
        $data['title'] = "Cuti | Dashboard";
        $this->template->load('master/master-app', 'app/dashboard', $data);
    }
}
