<div class="row">
  <div class="col-md-12 col-sm-12 col-xs-12">
    <div class="x_panel">
      <div class="x_title">
        <h2>Form Pengajuan Cuti <small>New Record </small></h2>
        <ul class="nav navbar-right panel_toolbox">
          <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><i class="fa fa-wrench"></i></a>
            <ul class="dropdown-menu" role="menu">
              <li><a href="#">Settings 1</a>
              </li>
              <li><a href="#">Settings 2</a>
              </li>
            </ul>
          </li>
          <li><a class="close-link"><i class="fa fa-close"></i></a>
          </li>
        </ul>
        <div class="clearfix"></div>
      </div>
      <div class="x_content">
        <br />
        <form id="demo-form2" data-parsley-validate class="form-horizontal form-label-left">

          <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12" for="NIP">NIP <span class="required">*</span>
            </label>
            <div class="col-md-6 col-sm-6 col-xs-12">
              <input type="text" id="NIP" required="required" class="form-control col-md-7 col-xs-12">
            </div>
          </div>
          <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12" for="Nama">Nama <span class="required">*</span>
            </label>
            <div class="col-md-6 col-sm-6 col-xs-12">
              <input type="text" id="nama" name="nama" required="required" class="form-control col-md-7 col-xs-12">
            </div>
          </div>
          <div class="form-group">
            <label for="jabatan" class="control-label col-md-3 col-sm-3 col-xs-12">Jabatan <span class="required">*</span>
            </label>
            <div class="col-md-6 col-sm-6 col-xs-12">
              <input id="jabatan" class="form-control col-md-7 col-xs-12" type="text" name="jabatan">
            </div>
          </div>

          <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12">Mulai Cuti</label>
              <div class="col-md-2 col-sm-4 col-xs-4">
                  <input type="text" class="form-control has-feedback-left" id="single_cal3" placeholder="First Name" aria-describedby="inputSuccess2Status3">
                  <span class="fa fa-calendar-o form-control-feedback left" aria-hidden="true"></span>
                  <span id="inputSuccess2Status3" class="sr-only">(success)</span>
                </div>
          </div>
          
          <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12">Mulai Cuti</label>
              <div class="col-md-2 col-sm-4 col-xs-4">
                <input type="text" class="form-control has-feedback-left" id="single_cal2" placeholder="First Name" aria-describedby="inputSuccess2Status2">
                <span class="fa fa-calendar-o form-control-feedback left" aria-hidden="true"></span>
                <span id="inputSuccess2Status2" class="sr-only">(success)</span>
              </div>
          </div>

          <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12">Jenis Cuti</label>
            <div class="col-md-2 col-sm-4 col-xs-4">
              <select class="form-control">
                <option>Choose option</option>
                <option>Option one</option>
                <option>Option two</option>
                <option>Option three</option>
                <option>Option four</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label for="keterangan" class="control-label col-md-3 col-sm-3 col-xs-12">Keterangan </span>
            </label>
            <div class="col-md-6 col-sm-6 col-xs-12">
              <textarea id='keterangan' required='required' rows='3' class='form-control' name='keterangan'></textarea>
            </div>
          </div>
          
          <div class="ln_solid"></div>
          <div class="form-group">
            <div class="col-md-6 col-sm-6 col-xs-12 col-md-offset-3">
              <button class="btn btn-primary" type="button">Cancel</button>
                <button class="btn btn-primary" type="reset">Reset</button>
              <button type="submit" class="btn btn-success">Submit</button>
            </div>
          </div>

        </form>
      </div>
    </div>
  </div>
</div>