import mysql.connector

while True:
    tabel = input("nama tabel : ")
    if tabel == "STOP IT":
        break
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="", database="ci_barang"
    )
    cursor = mydb.cursor()
    cursor.execute("SHOW columns FROM " + tabel + "")
    result = cursor.fetchall()
    kolom = []
    for x in result:
        kolom.append(x[0])

    panjangdata = len(kolom)
    iterasi = 0
    f = open("controllers/" + tabel + ".php", "w+")

    f.write("<?php \n")
    f.write("require APPPATH . 'libraries/REST_Controller.php'; \n")
    f.write("class " + tabel + " extends REST_Controller{\n")
    f.write("    public function __construct(){\n")
    f.write("        parent::__construct();\n")
    f.write("        $this->load->model('Model" + tabel + "','" + tabel + "');\n")
    f.write("    }\n")
    f.write("    public function index_get(){\n")
    f.write("        $" + kolom[0] + "=$this->get('" + kolom[0] + "');\n")
    f.write("        if($" + kolom[0] + "===null){\n")
    f.write(
        "            $data"
        + tabel
        + "= $this->"
        + tabel
        + "->getData"
        + tabel
        + "();\n"
    )
    f.write("        }else{ \n")
    f.write(
        "            $data"
        + tabel
        + "= $this->"
        + tabel
        + "->getData"
        + tabel
        + "($"
        + kolom[0]
        + ");\n"
    )
    f.write("        }\n")
    f.write("        if($data" + tabel + "){\n")
    f.write("            $this->response(\n")
    f.write("                [\n")
    f.write("                    'status'=>true,\n")
    f.write("                    'data_person' => $data" + tabel + "\n")
    f.write("                ],\n")
    f.write("                REST_Controller::HTTP_OK\n")
    f.write("            );\n")
    f.write("        }else{\n")
    f.write("            $this->response(\n")
    f.write("                [\n")
    f.write("                    'status'=>false,\n")
    f.write("                    'data_person' => \"Data tidak ditemukan\"\n")
    f.write("                ],\n")
    f.write("                REST_Controller::HTTP_NOT_FOUND\n")
    f.write("            );\n")
    f.write("        }\n")
    f.write("    }\n")
    f.write("    public function index_post(){\n")
    for x in kolom:
        f.write("        $" + x + "=$this->post('" + x + "');\n")
    f.write("        $data = [\n")
    for x in kolom:
        f.write("            '" + x + "' => $" + x + ",\n")
    f.write("        ];\n")
    f.write("        if( ")
    for x in kolom:
        f.write("$" + x + " === null ")
        if panjangdata - 1 > iterasi:
            f.write("|| ")
            iterasi += 1
    iterasi = 0
    f.write("){\n")
    f.write("            $this->response(\n")
    f.write("                [\n")
    f.write("                    'status' => false,\n")
    f.write(
        "                    'message' => 'data yang dikirimkan tidak boleh ada yang kosong'\n"
    )
    f.write("                ],\n")
    f.write("                REST_Controller::HTTP_BAD_REQUEST\n")
    f.write("            );\n")
    f.write("        }else{\n")
    f.write("            if($this->" + tabel + "->tambah" + tabel + "($data)>0){\n")
    f.write("                $this->response(\n")
    f.write("                    [\n")
    f.write("                        'status' => true,\n")
    f.write("                        'message' => 'data berhasil ditambahkan'\n")
    f.write("                    ],\n")
    f.write("                    REST_Controller::HTTP_CREATED\n")
    f.write("                );\n")
    f.write("            }\n")
    f.write("            else{\n")
    f.write("                $this->response(\n")
    f.write("                    [\n")
    f.write("                        'status' => false,\n")
    f.write("                        'message' => 'Gagal menambahkan data'\n")
    f.write("                    ],\n")
    f.write("                    REST_Controller::HTTP_BAD_REQUEST\n")
    f.write("                );\n")
    f.write("            }\n")
    f.write("        }\n")
    f.write("    }\n")
    f.write("    public function index_delete(){\n")
    f.write("        $" + kolom[0] + " = $this->delete('" + kolom[0] + "');\n")
    f.write("        if($" + kolom[0] + "===null){\n")
    f.write("            $this->response(\n")
    f.write("                [\n")
    f.write("                    'status' => false,\n")
    f.write("                    'message' => '" + kolom[0] + " tidak boleh kosong'\n")
    f.write("                ],\n")
    f.write("                REST_Controller::HTTP_BAD_REQUEST\n")
    f.write("            );\n")
    f.write("        }\n")
    f.write("        else{\n")
    f.write(
        "            if($this->"
        + tabel
        + "->hapus"
        + tabel
        + "($"
        + kolom[0]
        + ")>0){\n"
    )
    f.write("                $this->response(\n")
    f.write("                    [\n")
    f.write("                        'status' => true,\n")
    f.write(
        "                        'message' => 'data "
        + tabel
        + " dengan "
        + kolom[0]
        + " : '.$"
        + kolom[0]
        + ".' berhasil dihapus'\n"
    )
    f.write("                    ],\n")
    f.write("                    REST_Controller::HTTP_OK\n")
    f.write("                );\n")
    f.write("            }\n")
    f.write("            else{\n")
    f.write("                $this->response(\n")
    f.write("                    [\n")
    f.write("                        'status' => false,\n")
    f.write(
        "                        'message' => 'data "
        + tabel
        + " dengan "
        + kolom[0]
        + " : '.$"
        + kolom[0]
        + ".' tidak ditemukan'\n"
    )
    f.write("                    ],\n")
    f.write("                    REST_Controller::HTTP_BAD_REQUEST\n")
    f.write("                );\n")
    f.write("            }\n")
    f.write("        }\n")
    f.write("\n")
    f.write("    }\n")
    f.write("    public function index_put(){\n")
    f.write("        $" + kolom[0] + " = $this->put('" + kolom[0] + "');\n")
    f.write("        $array" + tabel + "=[\n")
    for x in kolom:

        if iterasi == 0:
            pass
        else:
            f.write("            '" + x + "' => $this->put('" + x + "'),\n")
        iterasi += 1

    f.write("        ];\n")
    f.write("        if($" + kolom[0] + "===null){\n")
    f.write("            $this->response(\n")
    f.write("                [\n")
    f.write("                    'status' => false,\n")
    f.write("                    'message' => '" + kolom[0] + " tidak boleh kosong'\n")
    f.write("                ],\n")
    f.write("                REST_Controller::HTTP_BAD_REQUEST\n")
    f.write("            );\n")
    f.write("        }\n")
    f.write("        else{\n")
    f.write(
        "            if($this->"
        + tabel
        + "->ubah"
        + tabel
        + "($array"
        + tabel
        + ",$"
        + kolom[0]
        + ")>0){\n"
    )
    f.write("                $this->response(\n")
    f.write("                    [\n")
    f.write("                        'status' => true,\n")
    f.write(
        "                        'message' => 'data "
        + tabel
        + " dengan "
        + kolom[0]
        + " : '.$"
        + kolom[0]
        + ".' berhasil diupdate'\n"
    )
    f.write("                    ],\n")
    f.write("                    REST_Controller::HTTP_OK\n")
    f.write("                );\n")
    f.write("            }\n")
    f.write("            else{\n")
    f.write("                $this->response(\n")
    f.write("                    [\n")
    f.write("                        'status' => false,\n")
    f.write("                        'message' => 'tidak ada data yang diupdate'\n")
    f.write("                    ],\n")
    f.write("                    REST_Controller::HTTP_BAD_REQUEST\n")
    f.write("                );\n")
    f.write("            }\n")
    f.write("        }\n")
    f.write("    }\n")
    f.write("    \n")
    f.write("\n")
    f.write("\n")
    f.write("}\n")

    f = open("models/Model" + tabel + ".php", "w+")
    f.write("<?php \n")
    f.write("class Model" + tabel + " extends CI_Model{ \n")
    f.write("    public function getData" + tabel + "($" + kolom[0] + "=null){ \n")
    f.write("        if($" + kolom[0] + "===null){ \n")
    f.write(
        "            $SemuaData"
        + tabel
        + ' = $this->db->get("'
        + tabel
        + ' ")->result();\n'
    )
    f.write("            return $SemuaData" + tabel + "; \n")
    f.write("        }else{ \n")
    f.write(
        "            $data_"
        + tabel
        + "_by"
        + kolom[0]
        + "=$this->db->get_where('"
        + tabel
        + "',['"
        + kolom[0]
        + "'=>$"
        + kolom[0]
        + "])->result(); \n"
    )
    f.write("            return $data_" + tabel + "_by" + kolom[0] + "; \n")
    f.write("        } \n")
    f.write("    } \n")
    f.write("    public function tambah" + tabel + "($data){ \n")
    f.write("        $this->db->insert('" + tabel + "',$data); \n")
    f.write("        return $this->db->affected_rows(); \n")
    f.write("    } \n")
    f.write("    public function hapus" + tabel + "($" + kolom[0] + "){ \n")
    f.write(
        "        $this->db->delete('"
        + tabel
        + "',['"
        + kolom[0]
        + "'=>$"
        + kolom[0]
        + "]); \n"
    )
    f.write("        return $this->db->affected_rows(); \n")
    f.write("    } \n")
    f.write("    public function ubah" + tabel + "($data,$" + kolom[0] + "){ \n")
    f.write(
        "        $this->db->update('"
        + tabel
        + "',$data, ['"
        + kolom[0]
        + "'=>$"
        + kolom[0]
        + "]);\n"
    )
    f.write("        return $this->db->affected_rows(); \n")
    f.write("    } \n")
    f.write("} \n")

