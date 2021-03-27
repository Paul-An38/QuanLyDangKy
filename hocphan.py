# coding=utf-8
from openerp.osv import fields,osv

class hocphan (osv.osv):
    _name='hocphan.danhsachhocphan'
    _columns = {
        #cac thuoc tinh cua lop book
        'tenhp':fields.char('Tên học phần', required=True, translate=True),
        'sotinchi':fields.integer('Số tín chỉ'),
        'hocphantienquyet':fields.selection([('tth','Toán tin học'),('nmw','Nhập môn web'),
                                ('ta1','Tiếng anh 1'),],'Học phần tiên quyết'),
        'tienquyet':fields.many2many('hocphan.danhsachhocphan','hocphan_tienquyet_rel', 'hocphan_id','tienquyet_id','Học phần tiên quyết')
    }
    _defaults={
        'sotinchi':0
    }

class lophocphan (osv.osv):
    _name='lophocphan.danhsachlophocphan'
    _columns = {
        #cac thuoc tinh cua lop book
        'malophocphan':fields.char('Mã lớp học phần', size=25, required=True, translate=True),
        'tenhocphan':fields.many2one('hocphan.danhsachhocphan',"Tên học phần", help="Học phần",required=True),
        'giangvien':fields.selection([('ttq','Trịnh Dình Quang'),('hqh','Hồ Quang Hiếu'),
                                ('tth','TRần Thái'),('ab','Alba')],'Giảng viên'),
        'ngaybd':fields.date('Ngày bắt đầu', required=False, readonly=False, select=True),
        'ngaykt':fields.date('Ngày kết thúc', required=False, readonly=False, select=True),
        'ghichu':fields.text('Ghi chú')
    }
    _defaults={
        'ngaybd':fields.datetime.now(),
        'ngaykt':fields.datetime.now()
    }


hocphan() #tao 1 the hien cho lop book_book
lophocphan()