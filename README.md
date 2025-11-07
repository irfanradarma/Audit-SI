<!-- Set language to Indonesian -->
<html lang="id" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Audit Sistem Informasi - Teuku Raja Irfan Radarma</title>
    
    <!-- Load Tailwind CSS for modern styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Use the Inter font family -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        // Custom Tailwind configuration
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                },
            },
        }
    </script>

    <!-- Removed the custom responsive table <style> block -->

</head>
<body class="bg-gray-100 font-sans text-gray-800">

    <!-- Main Content Container -->
    <!-- Added max-w-7xl for better large-screen readability -->
    <div class="max-w-7xl mx-auto p-4 sm:p-6 md:p-10">
        
        <!-- Page Header -->
        <header class="mb-8 p-6 bg-white rounded-xl shadow-md">
            <h1 class="text-3xl md:text-4xl font-bold text-gray-900">
                Audit Sistem Informasi
            </h1>
            <p class="mt-2 text-lg text-gray-600">
                by Teuku Raja Irfan Radarma
            </p>
        </header>

        <!-- Main Card for Content -->
        <main class="bg-white rounded-xl shadow-md overflow-hidden">
            
            <!-- Link Section -->
            <div class="p-6 border-b border-gray-200">
                <h2 class="text-2xl font-semibold mb-4">Materi Penting</h2>
                <a href="https://github.com/irfanradarma/Audit-SI/blob/main/ASP%20STR_2514926D_Audit%20Sistem%20Informasi.pdf" 
                   target="_blank" 
                   rel="noopener noreferrer"
                   <!-- Button is full-width on small screens, auto-width on larger -->
                   class="inline-flex items-center justify-center gap-2 w-full sm:w-auto bg-blue-600 text-white font-semibold py-2 px-5 rounded-lg hover:bg-blue-700 transition-colors duration-200 shadow-sm">
                    <!-- Simple SVG icon for download -->
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                    </svg>
                    Unduh Rencana Pembelajaran Semester (RPS)
                </a>
            </div>

            <!-- Materials Table Section -->
            <div class="p-6">
                <h3 class="text-2xl font-semibold mb-5">Bahan Perkuliahan</h3>
                
                <!-- Table container for horizontal scrolling on small screens -->
                <div class="overflow-x-auto">
                    <table class="w-full min-w-[600px] border border-gray-400 border-collapse">
                        <!-- Table Header -->
                        <thead class="bg-gray-200 text-gray-700">
                            <tr>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider border border-gray-300">No</th>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider border border-gray-300">Topik</th>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider border border-gray-300">Bahan Ajar</th>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider border border-gray-300">Praktikum</th>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider border border-gray-300">Lain-Lain</th>
                            </tr>
                        </thead>
                        
                        <!-- Table Body -->
                        <tbody>
                            <!-- Rows 1-6 with placeholder content -->
                            <tr>
                                <td class="p-3 border border-gray-300">1</td>
                                <td class="p-3 border border-gray-300">Pendahuluan Audit SI</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 1</a></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Lab 1</a></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">2</td>
                                <td class="p-3 border border-gray-300">Standar dan Kerangka Kerja Audit (COBIT)</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 2</a></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Lab 2</a></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Link COBIT</a></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">3</td>
                                <td class="p-3 border border-gray-300">Manajemen Risiko TI</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 3</a></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Studi Kasus 1</a></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">4</td>
                                <td class="p-3 border border-gray-300">Audit Tata Kelola (IT Governance)</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 4</a></td>
                                <td class="p-3 border border-gray-300"></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">5</td>
                                <td class="p-3 border border-gray-300">Audit Kontrol Aplikasi</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 5</a></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Lab 3</a></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">6</td>
                                <td class="p-3 border border-gray-300">Audit Infrastruktur dan Jaringan</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 6</a></td>
                                <td class="p-3 border border-gray-300"></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Video</a></td>
                            </tr>
                            
                            <!-- Row 7: Review -->
                            <tr>
                                <td class="p-3 border border-gray-300">7</td>
                                <td class="p-3 border border-gray-300" colspan="4">Review Materi 1-6</td>
                            </tr>

                            <!-- Row 8: Midterm Exam (UTS) -->
                            <tr class="bg-blue-50 text-blue-800 font-semibold text-center">
                                <td class="p-3 border border-gray-300">8</td>
                                <td class="p-3 border border-gray-300" colspan="4">Ujian Tengah Semester (UTS)</td>
                            </tr>

                            <!-- Rows 9-14 with placeholder content -->
                            <tr>
                                <td class="p-3 border border-gray-300">9</td>
                                <td class="p-3 border border-gray-300">Teknik Audit Berbantuan Komputer (TABK)</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 7</a></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Lab 4 (ACL)</a></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">10</td>
                                <td class="p-3 border border-gray-300">Audit Keamanan Fisik dan Lingkungan</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 8</a></td>
                                <td class="p-3 border border-gray-300"></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">11</td>
                                <td class="p-3 border border-gray-300">Audit Business Continuity Planning (BCP)</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 9</a></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Studi Kasus 2</a></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">12</td>
                                <td class="p-3 border border-gray-300">Audit Proyek Pengembangan Sistem</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 10</a></td>
                                <td class="p-3 border border-gray-300"></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">13</td>
                                <td class="p-3 border border-gray-300">Laporan Audit SI</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 11</a></td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Contoh Laporan</a></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            <tr>
                                <td class="p-3 border border-gray-300">14</td>
                                <td class="p-3 border border-gray-300">Etika Profesi Audit</td>
                                <td class="p-3 border border-gray-300"><a href="#" class="text-blue-600 hover:underline">Slide 12</a></td>
                                <td class="p-3 border border-gray-300"></td>
                                <td class="p-3 border border-gray-300"></td>
                            </tr>
                            
                            <!-- Row 15: Review -->
                            <tr>
                                <td class="p-3 border border-gray-300">15</td>
                                <td class="p-3 border border-gray-300" colspan="4">Review Materi 9-14 / Presentasi Proyek</td>
                            </tr>
                            
                            <!-- Row 16: Final Exam (UAS) -->
                            <tr class="bg-green-50 text-green-800 font-semibold text-center">
                                <td class="p-3 border border-gray-300">16</td>
                                <td class="p-3 border border-gray-300" colspan="4">Ujian Akhir Semester (UAS)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
        </main>
        
        <!-- Footer -->
        <footer class="text-center mt-8 p-4 text-gray-500 text-sm">
            <p>&copy; 2025 Teuku Raja Irfan Radarma. Dibuat untuk GitHub Pages.</p>
        </footer>
        
    </div> <!-- end container -->

</body>
</html>