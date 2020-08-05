#!/usr/bin/env python3

import sys
from PyPDF2 import PdfFileMerger


merger = PdfFileMerger()
merger.append(sys.argv[1])
merger.append(sys.argv[2])
merger.write(sys.argv[3])
merger.close()
