<?php
defined('BASEPATH') or exit('No direct script access allowed');

class Approve extends CI_Controller
{
    public function __construct()
    {
        parent::__construct();
       
    }

    public function index()
    {
        $data['title'] = "Cuti | Approve";
        $this->template->load('master/master-app', 'app/approve_cuti', $data);
    }
}
