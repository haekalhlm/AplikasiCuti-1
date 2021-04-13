<?php 
class Modelbarang extends CI_Model{ 
    public function getDatabarang($id_barang=null){ 
        if($id_barang===null){ 
            $SemuaDatabarang = $this->db->get("barang ")->result();
            return $SemuaDatabarang; 
        }else{ 
            $data_barang_byid_barang=$this->db->get_where('barang',['id_barang'=>$id_barang])->result(); 
            return $data_barang_byid_barang; 
        } 
    } 
    public function tambahbarang($data){ 
        $this->db->insert('barang',$data); 
        return $this->db->affected_rows(); 
    } 
    public function hapusbarang($id_barang){ 
        $this->db->delete('barang',['id_barang'=>$id_barang]); 
        return $this->db->affected_rows(); 
    } 
    public function ubahbarang($data,$id_barang){ 
        $this->db->update('barang',$data, ['id_barang'=>$id_barang]);
        return $this->db->affected_rows(); 
    } 
} 
