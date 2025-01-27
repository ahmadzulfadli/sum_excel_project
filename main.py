from DBClass import *
import uuid
import os

from DataProcessor import DataProcessor

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    path_save = os.path.join(os.path.dirname(__file__), "data/upload/")

    if 'uploaded_file' not in request.files:
        flash('Tidak ada file yang diunggah.')
        return redirect(url_for('index'))

    file = request.files['uploaded_file']

    transaction_id = str(uuid.uuid4())
    sheet_name = request.form.get('sheet_name')
    column_name = request.form.get('column_name')
    header_number = request.form.get('header_number')
    name = request.form.get('name')
    address = request.form.get('address')
    email = request.form.get('email')

    if not name or not address or not email:
        flash('Semua kolom harus diisi.')
        return redirect(url_for('index'))

    if file.filename == '':
        flash('Tidak ada file yang dipilih.')
        return redirect(url_for('index'))

    if file and file.filename.endswith('.zip'):
        filename = f"{transaction_id}.zip"
        save_path = os.path.join(path_save, filename)
        file.save(save_path)

        # save exstract to database
        create_data = SumExcelTransactions(
            transaction_id=transaction_id,
            sheet_name=sheet_name,
            column_name=column_name,
            header_number=header_number,
            name=name,
            address=address,
            email=email,
            status_transaction=f"File berhasil diunggah oleh {name}"
        )

        db.session.add(create_data)
        db.session.commit()

        # Proses file
        column_list = [col.strip() for col in column_name.split(',')]
        process = DataProcessor(transaction_id, sheet_name, column_list, header_number)
        process.run()

        # Flash message untuk konfirmasi
        flash(f"File berhasil diunggah oleh {name}.")
        return redirect(url_for('success', status=True, filename=transaction_id))
    else:
        flash('File harus berformat ZIP.')
        return redirect(url_for('index'))

@app.route('/success')
def success():
    status = request.args.get('status')
    filename = request.args.get('filename')
    return render_template('success.html', status=status, filename=filename)

@app.route('/download-excel')
def download_excel():
    filename = request.args.get('filename')
    path_save = os.path.join(os.path.dirname(__file__), f"data/results/excel/hasil_perhitungan_{filename}.xlsx")
    if os.path.exists(path_save):
        return send_file(path_save, as_attachment=True)
    else:
        flash('File results belum tersedia.')

@app.route('/download-grafik')
def download_img():
    filename = request.args.get('filename')
    path_save = os.path.join(os.path.dirname(__file__), f"data/results/img/grafik_{filename}.png")
    if os.path.exists(path_save):
        return send_file(path_save, as_attachment=True)
    else:
        flash('File results belum tersedia.')

if __name__ == '__main__':
    app.run()
