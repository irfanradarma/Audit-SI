<!DOCTYPE html>
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

    <!-- 
      *** CUSTOM RESPONSIVE TABLE STYLES ***
      This CSS block handles the mobile view of the table.
      - On screens smaller than 'md' (768px), it hides the table header.
      - It styles each table row (<tr>) as a self-contained card.
      - It stacks table cells (<td>) vertically.
      - It uses the 'data-label' attribute from the HTML to create a text label for each cell,
        making the card easy to understand.
    -->
    <style>
        @media (max-width: 767px) { /* Tailwind's 'md' breakpoint */
            .responsive-table thead {
                display: none; /* Hide table headers on mobile */
            }
            .responsive-table tbody,
            .responsive-table tr {
                display: block;
                width: 100%;
            }
            .responsive-table tr {
                /* Style each row as a card */
                border: 1px solid #e5e7eb; /* gray-200 */
                border-radius: 0.75rem; /* rounded-xl */
                margin-bottom: 1rem; /* mb-4 */
                overflow: hidden; /* To contain rounded corners */
                box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06); /* shadow-sm */
            }
            /* Special handling for exam/review rows */
            .responsive-table tr.exam-row,
            .responsive-table tr.review-row {
                display: flex;
                padding: 0.75rem 1rem; /* p-3 + horizontal padding */
                justify-content: center;
                align-items: center;
                text-align: center;
            }
            .responsive-table td {
                display: block;
                width: 100%;
                position: relative;
                padding: 0.75rem; /* p-3 */
                padding-left: 50%; /* Make space for the label */
                text-align: right;
                border-bottom: 1px solid #f3f4f6; /* gray-100 */
            }
            .responsive-table tr:last-child td:last-child,
            .responsive-table tr td:last-child {
                border-bottom: 0; /* No border on the last cell in a card */
            }
            .responsive-table td::before {
                /* Add the data label as a pseudo-element */
                content: attr(data-label);
                position: absolute;
                left: 0.75rem; /* p-3 */
                width: 45%; /* Corresponds to padding-left */
                text-align: left;
                font-weight: 600; /* semibold */
                color: #374151; /* gray-700 */
            }
            /* Hide cells with no content for "Lain-Lain" etc. */
            .responsive-table td[data-label]:empty {
                display: none;
            }
            /* Handle colspan for special rows */
            .responsive-table td[colspan="4"] {
                padding-left: 0.75rem; /* p-3 */
                text-align: center;
            }
            .responsive-table td[colspan="4"]::before {
                display: none; /* No label for colspan cells */
            }
        }
    </style>
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
                
                <!-- 
                  *** RESPONSIVE TABLE ***
                  - 'responsive-table' class links to the <style> block.
                  - On 'md' screens and up, it behaves like a normal table with a border.
                  - On mobile, the <style> block takes over.
                -->
                <div class="w-full md:rounded-lg md:border md:border-gray-200 md:overflow-hidden">
                    <table class="responsive-table w-full border-collapse">
                        <!-- Table Header: Hidden on mobile, visible on desktop -->
                        <thead class="hidden md:table-header-group bg-gray-800 text-white">
                            <tr>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider">No</th>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider">Topik</th>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider">Bahan Ajar</th>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider">Praktikum</th>
                                <th class="p-3 text-left text-sm font-semibold uppercase tracking-wider">Lain-Lain</th>
                            </tr>
                        </thead>
                        
                        <!-- Table Body: Becomes block on mobile, rows become cards -->
                        <tbody class="block md:table-row-group md:divide-y md:divide-gray-200">
                            <!-- Each <td> now has a 'data-label' attribute for the mobile view -->
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">1</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Pendahuluan Audit SI</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 1</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Lab 1</a></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">2</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Standar dan Kerangka Kerja Audit (COBIT)</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 2</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Lab 2</a></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Link COBIT</a></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">3</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Manajemen Risiko TI</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 3</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Studi Kasus 1</a></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">4</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Audit Tata Kelola (IT Governance)</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 4</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">5</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Audit Kontrol Aplikasi</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 5</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Lab 3</a></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">6</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Audit Infrastruktur dan Jaringan</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 6</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Video</a></td>
                            </tr>
                            
                            <!-- Row 7: Review -->
                            <tr class="review-row block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">7</td>
                                <td colspan="4" class="block md:table-cell p-3">Review Materi 1-6</td>
                            </tr>

                            <!-- Row 8: Midterm Exam (UTS) -->
                            <tr class="exam-row bg-blue-50 text-blue-800 font-semibold block md:table-row text-center">
                                <td data-label="No" class="block md:table-cell p-3">8</td>
                                <td colspan="4" class="block md:table-cell p-3">Ujian Tengah Semester (UTS)</td>
                            </tr>

                            <!-- Rows 9-14 -->
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">9</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Teknik Audit Berbantuan Komputer (TABK)</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 7</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Lab 4 (ACL)</a></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">10</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Audit Keamanan Fisik dan Lingkungan</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 8</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">11</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Audit Business Continuity Planning (BCP)</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 9</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Studi Kasus 2</a></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">12</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Audit Proyek Pengembangan Sistem</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 10</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">13</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Laporan Audit SI</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 11</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Contoh Laporan</a></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            <tr class="block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">14</td>
                                <td data-label="Topik" class="block md:table-cell p-3 break-words">Etika Profesi Audit</td>
                                <td data-label="Bahan Ajar" class="block md:table-cell p-3"><a href="#" class="text-blue-600 hover:underline">Slide 12</a></td>
                                <td data-label="Praktikum" class="block md:table-cell p-3"></td>
                                <td data-label="Lain-Lain" class="block md:table-cell p-3"></td>
                            </tr>
                            
                            <!-- Row 15: Review -->
                            <tr class="review-row block md:table-row md:hover:bg-gray-50 md:even:bg-gray-50">
                                <td data-label="No" class="block md:table-cell p-3">15</td>
                                <td colspan="4" class="block md:table-cell p-3">Review Materi 9-14 / Presentasi Proyek</td>
                            </tr>
                            
                            <!-- Row 16: Final Exam (UAS) -->
                            <tr class="exam-row bg-green-50 text-green-800 font-semibold block md:table-row text-center">
                                <td data-label="No" class="block md:table-cell p-3">16</td>
                                <td colspan="4" class="block md:table-cell p-3">Ujian Akhir Semester (UAS)</td>
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